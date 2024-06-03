# StopWatch

This Python stopwatch application offers basic functionality with three main functions: start, stop, and reset. It provides a simple yet effective way to measure elapsed time for various tasks or activities.

* * *

#### Usage

- Start: Initiate the stopwatch to begin timing. 
- Stop: Pause the stopwatch to halt timing. 
- Reset: Reset the stopwatch to zero to start timing anew.

This stopwatch can be easily integrated into Python projects requiring time tracking or management. It's a lightweight solution for time measurement needs.

* * *

#### Build the executable

```shell
git clone https://github.com/ghostreaver/stopwatch
cd stopwatch
python3 -m pip install -r requirement.txt
python3 builder.py -o "stopwatch"
``` 

* * *

#### Possible issues

```shell
Cannot find reference 'connect' in 'pyqtSignal | pyqtSignal | function'
```

To correct this bug, you will need to edit the stub file named `QtCore.pyi`, which can be found in `/site-packages/PyQt6`. After opening `QtCore.pyi`, make sure you see both of the `def connect()` lines and both of the `def emit()` lines below. If they are missing, you can add them, and the relevant warnings should disappear.

```shell
# Support for new-style signals and slots.
class pyqtSignal:

    signatures = ...    # type: typing.Tuple[str, ...]

    def __init__(self, *types: typing.Any, name: str = ...) -> None: ...

    @typing.overload
    def __get__(self, instance: None, owner: typing.Type['QObject']) -> 'pyqtSignal': ...

    @typing.overload
    def __get__(self, instance: 'QObject', owner: typing.Type['QObject']) -> 'pyqtBoundSignal': ...

    # Bug fix related to 'connect()' warning
    def connect(self, slot: 'PYQT_SLOT') -> 'QMetaObject.Connection': ...
    def emit(self, *args: typing.Any) -> None: ...
```