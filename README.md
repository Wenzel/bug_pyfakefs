# bug_pyfakefs

## setup

    virtualenv -p python3 venv
    source ./venv/bin/activate
    (venv) pip install -r requirements.txt
    python -m pytest -v --pdb

## bug

~~~Python3
venv/lib/python3.8/site-packages/libcloud/storage/drivers/local.py:89: in __enter__
    success = self.ipc_lock.acquire(blocking=True,
venv/lib/python3.8/site-packages/fasteners/process_lock.py:135: in acquire
    self._do_open()
venv/lib/python3.8/site-packages/fasteners/process_lock.py:107: in _do_open
    self.lockfile = open(self.path, 'a')
venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:4624: in open
    return fake_open(file, mode, buffering, encoding, errors,
venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:5202: in __call__
    return self.call(*args, **kwargs)
venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:5263: in call
    file_object = self._init_file_object(file_object,
venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:5330: in _init_file_object
    file_object = self.filesystem.create_file_internally(
venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:2608: in create_file_internally
    self.raise_os_error(errno.ENOENT, parent_directory)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <pyfakefs.fake_filesystem.FakeFilesystem object at 0x7f94c2304ac0>, errno = 2, filename = b'/tmp', winerror = None

    def raise_os_error(self, errno, filename=None, winerror=None):
        """Raises OSError.
        The error message is constructed from the given error code and shall
        start with the error string issued in the real system.
        Note: this is not true under Windows if winerror is given - in this
        case a localized message specific to winerror will be shown in the
        real file system.

        Args:
            errno: A numeric error code from the C variable errno.
            filename: The name of the affected file, if any.
            winerror: Windows only - the specific Windows error code.
        """
        message = self._error_message(errno)
        if (winerror is not None and sys.platform == 'win32' and
                self.is_windows_fs):
            raise OSError(errno, message, filename, winerror)
>       raise OSError(errno, message, filename)
E       FileNotFoundError: [Errno 2] No such file or directory in the fake filesystem: b'/tmp'

venv/lib/python3.8/site-packages/pyfakefs/fake_filesystem.py:1010: FileNotFoundError
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
~~~
