1. Generate one asymmetric key pair (public and private keys)
    ```bash
    openssl genrsa -out $key_file_name 4096
    openssl rsa -in $key_file_name -pubout > $key_file_name.pub
    ```

1. Export both file's path to your environment with the following identifiers
    - Default is "$HOME/.rsa_keys/pswd[.pub]"
    ```bash
    export PSWD_PATH_PUBK="$key_file_name.pub"
    export PSWD_PATH_PRIK="$key_file_name"
    ```

1. (Optional). To customize the secrets file, use export to your environment with this identifier
    - Default is "$HOME/.pswd[.bkp]"
    ```bash
    export PSWD_PATH_FILE="$pass_file_name"
    ```

