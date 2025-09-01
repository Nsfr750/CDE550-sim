# Configuration Guide

This guide explains how to configure CDE550-sim to suit your needs.

## Configuration Files

CDE550-sim can be configured using the following methods (in order of precedence):

1. Command-line arguments
2. Environment variables
3. Configuration file (`config.ini` in the application directory)
4. Default values

## Configuration Options

### Main Configuration (`config.ini`)

```ini
[general]
# Enable or disable debug mode
debug = false

# Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
log_level = INFO

[server]
# Server host
host = 0.0.0.0

# Server port
port = 8000

# Enable HTTPS
enable_https = false

[database]
# Database connection string
db_url = sqlite:///data.db

# Maximum number of database connections
max_connections = 10
```

### Environment Variables

All configuration options can be set using environment variables with the `CDE550_` prefix:

```bash
export CDE550_GENERAL_DEBUG=true
export CDE550_SERVER_PORT=8080
```

## Advanced Configuration

### Logging Configuration

You can customize the logging behavior by creating a `logging.ini` file in the configuration directory.

### Custom Plugins

To add custom plugins, place them in the `plugins/` directory and update the configuration:

```ini
[plugins]
enabled_plugins = plugin1,plugin2,plugin3
```

## Verifying Configuration

To verify your configuration, run:

```bash
python main.py --check-config
```

## Best Practices

1. Never commit sensitive information (passwords, API keys) to version control
2. Use environment variables for sensitive data
3. Document all configuration changes in your team
4. Test configuration changes in a development environment first

## Troubleshooting

If you encounter configuration issues, check the following:

1. File permissions
2. Environment variable names and values
3. Configuration file syntax
4. Log files for specific error messages
