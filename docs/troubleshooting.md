# Troubleshooting Guide

This guide helps you identify and resolve common issues with CDE550-sim.

## Common Issues

### 1. Installation Issues

#### Error: Module not found

**Symptom**:
```
ModuleNotFoundError: No module named 'module_name'
```

**Solution**:
```bash
pip install -r requirements.txt
```

### 2. Runtime Errors

#### Application Crashes on Startup

**Possible Causes**:
- Missing configuration file
- Database connection issues
- Permission problems

**Solution**:
1. Verify all required files are in place
2. Check file permissions
3. Run with `--verbose` for more details

## Error Codes

| Code | Description | Solution |
|------|-------------|-----------|
| 1001 | Database connection failed | Check database URL and credentials |
| 1002 | Invalid configuration | Verify config.ini file |
| 1003 | Missing dependencies | Run `pip install -r requirements.txt` |

## Log Files

Logs are stored in:
- Windows: `%APPDATA%\CDE550-sim\logs\`
- Linux/Mac: `~/.config/CDE550-sim/logs/`

## Getting Help

If you can't resolve your issue:
1. Check the logs for error messages
2. Search the [GitHub issues](https://github.com/Nsfr750/CDE550-sim/issues)
3. [Open a new issue](https://github.com/Nsfr750/CDE550-sim/issues/new/choose) with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Log files (redact sensitive info)
   - System information

## Known Issues

- [ ] Issue #123: [Brief description]
- [ ] Issue #124: [Brief description]

## Support

For additional help, join our [Discord server](https://discord.gg/ryqNeuRYjD).
