# For Watching changes files
Try `nodemon` global package (local package do not work with import file location) inside specific folder

### Example
```
cd linear-regression
nodemon ./lr_1d.py
```

## npm 2 and newer
It's possible to pass args to npm run since npm 2 (2014). The syntax is as follows:

    npm run <command> [-- <args>]

Note the -- separator, used to separate the params passed to npm command itself, and the params passed to your script.

With the example package.json:
```
  "scripts": {
    "grunt": "grunt",
    "server": "node server.js"
  }
```
here's how to pass the params to those scripts:

```
npm run grunt -- task:target  // invokes `grunt task:target`
npm run server -- --port=1337 // invokes `node server.js --port=1337`
```
Note: If your param does not start with - or --, then having an explicit -- separator is not needed; but it's better to do it anyway for clarity.

```
npm run grunt task:target     // invokes `grunt task:target`
```