# Dotbot duti plugin

Instant customization of file associations with `dotbot`

## Requirements

You need [`dotbot`](https://github.com/anishathalye/dotbot) and [`duti`](https://github.com/moretension/duti) to be installed first.


## Installation

1. As is the case with `dotbot`, first, add this plugin as a submodule to your dotfiles repo: 

```bash
git submodule add https://github.com/andrejreznik/dotbot-duti.git
```

2. Modify your `./install` with new plugin directory: 

```bash
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASEDIR}" --plugin-dir dotbot-duti -c "${CONFIG}" "${@}"
```

3. Add path to `duti` settings file to your [`install.conf.yaml`](/example.yaml):

```yaml
- duti:
    file: Dutifile
```

## License 

MIT. See [LICENSE](/LICENSE) for more details.
