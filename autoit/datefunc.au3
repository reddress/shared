#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#include <FileConstants.au3>

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("date functions", 600, 120, 350, 380)
WinSetOnTop("date functions", "", 1)

$the_date = GUICtrlCreateInput("", 20, 10, 56, 19)

$the_button = GUICtrlCreateButton("btn01", 90, 40, 60)

GUICtrlSetOnEvent($the_button, "fnLoad")

Func fnLoad()
   For $i = 1 To @MON
	  GUICtrlSetData($the_date, GUICtrlRead($the_date) & @MON)
   Next
EndFunc

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
Func CLOSEClicked()
   Exit
EndFunc

GUISetState(@SW_SHOW)
While 1
   Sleep(100)
WEnd