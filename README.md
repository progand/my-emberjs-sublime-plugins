# my-emberjs-sublime-plugins

This package contains my sublime packages for Emberjs development. This is personal packages and might not suit your need althouth code is free.


## RelatedEmberFiles

Opens related emberjs files:
 - opens corresponding `.js` or `.hbs` component file
 - opens corresponding route & controller & template files if exist

### Example keybinding

```
[
...
{ "keys": ["alt+s"], "command": "related_ember_files" },
...
]
```

## MyPrettier

Runs local Prettier to format entire saved file. Selection or buffer format is not supported yet.

### Example keybinding

```
[
...
{ "keys": ["ctrl+alt+f"], "command": "my_prettier" },
...
]