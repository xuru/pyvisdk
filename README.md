
# pyvisdk - vSphere SDK  for Python

  [pyvisdk](http://xuru.github.com/pyvisdk) is a pure python library to access the [VMware vSphere web services API](http://www.vmware.com/support/developer/vc-sdk/).
  Thanks to [psphere](http://jkinred.bitbucket.org/psphere/index.html) for giving me some insight into how the API works.

## Installation
  This will be uploaded to the Python Package Index when it becomes more stable, but for now you can download the code from github, then run:
  $ sudo python ./setup.py install
  
## Features
  A more Object Oriented approach to interfacing with the web services API.
  Knowledge of the inner workings of the API is not needed.
  Simple and clean interface.

## Example
    vim = Vim("vcenter.company.com")
    vim.login(username, password)

    machine = vim.getVirtualMachineByName("MyTestMachine")
    snapshot = machine.createSnapshot()
    print "Created snapshot: %s" % snapshot.name

## Authors

  * TJ Holowaychuk


## License 

(The MIT License)

Copyright (c) 2011 Eric Plaster &lt;plaster at gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.