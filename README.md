## GitLab Pages Configuration

The GitLab Pages domain name is defined in the `config/gitlab.rb` configuration file or directly in the Docker Compose manifest with `pages_external_url`:

```shell
# GitLab Pages
pages_external_url 'https://gitlab-pages.jklug.work'  # Define GitLab Page domain name
gitlab_pages['enable'] = true
pages_nginx['redirect_http_to_https'] = true
pages_nginx['ssl_certificate'] = "/etc/gitlab/ssl/fullchain.pem"
pages_nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/privkey.pem"
## GitLab Pages: Storage Configuration
gitlab_rails['pages_local_store_enabled'] = true
gitlab_rails['pages_local_store_path'] = "/var/opt/gitlab/gitlab-rails/shared/pages"
```

<br>

## DNS

- Make sure the domain name of the GitLab page subdomain can be resolved by the clients

<br>

## Requirements

- Make sure the add `coverage` in the requirements.txt file.