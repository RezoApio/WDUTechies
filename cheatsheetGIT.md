# Proxy with Git

## Setting config

```bash
git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080
```

        change proxyuser to your proxy user
        change proxypwd to your proxy password
        change proxy.server.com to the URL of your proxy server
        change 8080 to the proxy port configured on your proxy server
        this is a change for all the repository

git config --local http.proxy http://10.225.92.1:80

git config --global http.https://github.com http://10.225.92.1:80
git config --global http.https://github.com.sslVerify false

## Checking config

```bash
git config --global --get http.proxy
```

## Unsetting Config

```shell
git config --global --unset http.proxy
```

## Adding Removing Alias

```shell
git config --global alias.tree "log --graph --decorate --pretty=oneline --abbrev-commit"
git config --global alias.pom "push origin master"
git config --global --unset alias.tree
```

# Another Wonderful command

