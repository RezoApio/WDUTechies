# Proxy with Git

## Setting config

```bash
git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080
```

        change proxyuser to your proxy user
        change proxypwd to your proxy password
        change proxy.server.com to the URL of your proxy server
        change 8080 to the proxy port configured on your proxy server


## Checking config

```bash
git config --global --get http.proxy
```


## Unsetting Config

```shell
git config --global --unset http.proxy
```


# Another Wonderful command