# redis_backup

Reliza backup do redis e armazena em S3AWS

## Testes de restore com Endpoints

### AWS:

`curl -X POST "http://127.0.0.1:8000/api/v1/restore?provider=aws&timestamp=2024-08-08_12-00-00"`

### Oracle Cloud:

`curl -X POST "http://127.0.0.1:8000/api/v1/restore?provider=oracle&timestamp=2024-08-08_12-00-00"`

### Google Cloud:

`curl -X POST "http://127.0.0.1:8000/api/v1/restore?provider=google&timestamp=2024-08-08_12-00-00"`

### NFS:

`curl -X POST "http://127.0.0.1:8000/api/v1/restore?provider=nfs&timestamp=2024-08-08_12-00-00"`

## Parametros

Os parametros de conexão deve ser fornecido via variável de ambiente ou arquivo `env`, as váriáveis de ambiente se sobrepõem ao arquivo `env` quando fornecidas.

| PARAMETRO                 | VLOR                                  | TIPO                                                                                               |
| ------------------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------- |
| AWS_ACCESS_KEY_ID         | your_aws_access_key_id                | Variável de ambiente cujo valor é a  chave de acesso ao AWS S3.                                |
| AWS_SECRET_ACCESS_KEY     | your_aws_secret_access_key            | Variável de ambiente cujo valor é a  senha de acesso ao AWS S3.                                 |
| AWS_BUCKET_NAME           | buckt_name                            | Variável de ambiente cujo valor é o nome do buckt  AWS S3.                                     |
| ORACLE_KEY_FILE           | /path/to/your/oracle/key_file.pem     | Variável de ambienete com o patah para o arquivo .pem contendo a chave de acesso ao Oracle Cloud. |
| ORACLE_BUCKET_NAME        | your_oracle_bucket_name               | Variável de ambinte cujo valor é o nome do bucket do Oracle Cloud.                               |
| ORACLE_NAMESPACE          | your_oracle_namespace                 | Variável de ambinte cujo valor é o nome do namespace do OracleCloud.                             |
| GOOGLE_CREDENTIALS_FILE   | /path/to/your/google/credentials.json | Variável de ambiente contendo o path para o arquivo Json com as credenciais do Google Cloud.      |
| GOOGLE_BUCKET_NAME        | your_google_bucket_name               | Variável de ambiente cujo valor é o nome dobucket Google Cloud.                                  |
| NFS_BACKUP_PATH           | /mnt/nfs/redis                        | Variável de ambiente cujo valor é o mount path NFS.                                              |
| REDIS_RDB_PATH            | /var/lib/redis/dump.rdb               | Váriáve de ambiente com path para o aqrquivo de dados do Redis (RDB file).                       |
| REDIS_AOF_PATH=path_redis | /var/lib/redis/appendonlydir/file.aof | Váriáve de ambiente com path para o aqrquivo de dados do Redis (AOF file).                       |

#### Uso:

Declare a variável diretamente no shell, ou adicione-as ao arquivo .bashrc ou profile.

```shell
export REDIS_AOF_PATH=path_redis
```

Editando arquivo ```.bashrc```:

```shell
vim .bashrc
```

Adicione ao final do arquivo as variáveis:

```shell
# Configurações da AWS
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_BUCKET_NAME=buckt_name

# # Configurações do Oracle Cloud
ORACLE_KEY_FILE=/path/to/your/oracle/key_file.pem
ORACLE_BUCKET_NAME=your_oracle_bucket_name
ORACLE_NAMESPACE=your_oracle_namespace

# # Configurações do Google Cloud
GOOGLE_CREDENTIALS_FILE=/path/to/your/google/credentials.json
GOOGLE_BUCKET_NAME=your_google_bucket_name

# # NFS mount path
NFS_BACKUP_PATH=/mnt/redis 

# # Redis path
REDIS_RDB_PATH=path/redis/rdb
REDIS_AOF_PATH=path/redis/aof

export REDIS_AOF_PATH="$REDIS_AOF_PAT" REDIS_RDB_PATH="$REDIS_RDB_PAT" AWS_ACCESS_KEY_ID="$AWS_ACCESS_KEY_I" ... ;


```

#### Usando um arquivo env

Declare na raiz do projeto um arquivo env contendo as variáveis

```shell
.evn
```

Conteúdo:

```shell
# Configurações da AWS
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_BUCKET_NAME=buckt_name

# # Configurações do Oracle Cloud
ORACLE_KEY_FILE=/path/to/your/oracle/key_file.pem
ORACLE_BUCKET_NAME=your_oracle_bucket_name
ORACLE_NAMESPACE=your_oracle_namespace

# # Configurações do Google Cloud
GOOGLE_CREDENTIALS_FILE=/path/to/your/google/credentials.json
GOOGLE_BUCKET_NAME=your_google_bucket_name

# # NFS mount path
NFS_BACKUP_PATH=/mnt/redis 

# # Redis path
REDIS_RDB_PATH=path/redis/rdb
REDIS_AOF_PATH=path/redis/aof
```

