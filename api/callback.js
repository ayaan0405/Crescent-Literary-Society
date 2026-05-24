module.exports = async function handler(req, res) {
  const { code } = req.query;
  const client_id = process.env.GITHUB_CLIENT_ID;
  const client_secret = process.env.GITHUB_CLIENT_SECRET;
  const redirect_uri = process.env.REDIRECT_URI || `https://${req.headers.host}/api/callback`;

  try {
    const response = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        client_id,
        client_secret,
        code,
        redirect_uri
      })
    });

    const data = await response.json();
    const token = data.access_token;
    
    if (!token) {
      throw new Error('Access token not found in response');
    }

    res.setHeader('Content-Type', 'text/html');
    res.status(200).send(`
      <script>
        const token = "${token}";
        const targetOrigin = window.location.origin;
        
        // 1. Send modern Decap CMS object format
        window.opener.postMessage(
          {
            type: 'authorization',
            payload: {
              token: token,
              provider: 'github'
            }
          },
          targetOrigin
        );

        // 2. Send legacy Netlify CMS string format as fallback
        window.opener.postMessage(
          'authorization:github:success:' + JSON.stringify({ token, provider: 'github' }),
          targetOrigin
        );

        window.close();
      </script>
    `);
  } catch (error) {
    res.status(500).send(`Authentication error: ${error.message}`);
  }
};
