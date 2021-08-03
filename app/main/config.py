class LocalConfig:
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:clive@localhost/dev_connector'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config_by_name = dict(
    LOCAL=LocalConfig
)