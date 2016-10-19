#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#include <ListViewConstants.au3>
#include <GuiListView.au3>

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Codigo History", 90, 120, 360, 580)
WinSetOnTop("Codigo History", "", 1)

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
$codigo = GUICtrlCreateInput("", 5, 5, 70, 19)

$button01 = GUICtrlCreateButton("141742", 5, 30, 70)
$button02 = GUICtrlCreateButton("141733A", 5, 60, 70)
$button03 = GUICtrlCreateButton("143208", 5, 90, 70)

;$buttonCopy = GUICtrlCreateButton("copy", 90, 40, 45)
;GUICtrlSetOnEvent($buttonNext, "fnNext")
;GUICtrlSetOnEvent($buttonCopy, "fnCopy")
;GUICtrlSetOnEvent($buttonAddUC, "addUC")

GUICtrlSetOnEvent($button01, "fnLoad01")
GUICtrlSetOnEvent($button02, "fnLoad02")
GUICtrlSetOnEvent($button03, "fnLoad03")

GUISetState(@SW_SHOW)
$oldcode = ""

GUICtrlSetOnEvent($codigo, "fnLoad00")
; HotKeySet("{F3}", "clearCodigo")

While 1
  Sleep(100)
WEnd

Func clearCodigo()
   GUICtrlSetData($codigo, "")
EndFunc

Func fnOpenProduto()
   WinActivate("Produto")
   Send("{F3}")
   ; MouseClick("left", 600, 55)
EndFunc

Func fnLoad00()
   Local $codigoLength = StringLen(GUICtrlRead($codigo))
   
   If $codigoLength < 6 Then
	  GUICtrlSetData($codigo, "")
   Else
	
	  fnOpenProduto()
	  Send(GUICtrlRead($codigo))
	  Send("{ENTER}")
   
   ;; add to ListView
	  addAsFirst()
	  resetState()
   EndIf
   
EndFunc

Func resetState()
   ;; reset state
   GUICtrlSetData($codigo, "")
   Sleep(500)
   MouseMove(380, 615, 3)
   MouseClick("left", 380, 615)
EndFunc

Func addAsFirst()
   ; MsgBox(0, "", _GUICtrlListView_GetItemCount($codigoList))
   
   ;If $count = 5 Then
   ;	_GUICtrlListView_DeleteItem($codigoList, 4)
   ;EndIf

     ; push codigos down
	  GUICtrlSetData($button03, GUICtrlRead($button02))
	  GUICtrlSetData($button02, GUICtrlRead($button01))
   
	  GUICtrlSetData($button01, StringUpper(GUICtrlRead($codigo)))
   
EndFunc

Func fnLoad01()
   fnOpenProduto()
   Send(GUICtrlRead($button01))
   Send("{ENTER}")
   resetState()
EndFunc

Func fnLoad02()
   fnOpenProduto()
   Send(GUICtrlRead($button02))
   Send("{ENTER}")
   resetState()
EndFunc

Func fnLoad03()
   fnOpenProduto()
   Send(GUICtrlRead($button03))
   Send("{ENTER}")
   resetState()
EndFunc


Func CLOSEClicked()
   Exit
EndFunc