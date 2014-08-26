javac -source 1.5 -target 1.5 -Xlint:-options -encoding utf8 %1.java
@if %ERRORLEVEL% == 0 (
java %1
)

