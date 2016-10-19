#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Cardex Jump", 600, 120, 0, 580)
WinSetOnTop("Cardex Jump", "", 1)

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
;$mylabel = GUICtrlCreateLabel("Version: May (update in June)", 30, 10)
$codigo = GUICtrlCreateInput("", 20, 10, 66, 19)

$button2012 = GUICtrlCreateButton("2012", 20, 40, 60)
$button2013 = GUICtrlCreateButton("2013", 90, 40, 60)
$button2012and13 = GUICtrlCreateButton("2012 xmas", 40, 70, 90)

$estoque = GUICtrlCreateInput("", 92, 10, 110, 19)
$notes = GUICtrlCreateEdit("Último container - ", 208, 10, 348, 100)

$buttonClip = GUICtrlCreateButton("copy", 166, 70)
$buttonClear = GUICtrlCreateButton("clear", 562, 10)
;$buttonAddUC = GUICtrlCreateButton("add UC", 550, 40)
GUICtrlSetOnEvent($button2012, "fnGen2012")
GUICtrlSetOnEvent($button2013, "fnGen2013")
GUICtrlSetOnEvent($button2012and13, "fnGen2012and13")
GUICtrlSetOnEvent($buttonClear, "fnClearEdit")
GUICtrlSetOnEvent($buttonClip, "fnCopyToClipboard")
;GUICtrlSetOnEvent($buttonAddUC, "addUC")

;$estoque = GUICtrlCreateEdit("", 172, 10, 70, 50, BitOR($ES_AUTOVSCROLL, $ES_AUTOHSCROLL, $ES_WANTRETURN))
GUISetState(@SW_SHOW)
$oldcode = ""

While 1
   $newcode = GUICtrlRead($codigo)
   If $oldcode <> $newcode Then
	  GUICtrlSetData($notes, "Último container - ")
	  GUICtrlSetData($estoque, "")
	  $oldcode = $newcode
   EndIf
   Sleep(100)
WEnd

Func fnClearEdit()
   GUICtrlSetData($notes, "")
   GUICtrlSetData($codigo, "")
EndFunc

Func addUC()
   GUICtrlSetData($notes, GUICtrlRead($notes) & @CRLF & "Último container - ")
EndFunc

Func fnCopyToClipboard()
   ClipPut(GUICtrlRead($notes))
EndFunc

;Func fnGen2013()
;   fnGeneric("{RIGHT}{DOWN}{DOWN}{DOWN}{DOWN}{RIGHT}")
;EndFunc

;Func fnGen2012()
;   fnGeneric("{RIGHT}{DOWN}{DOWN}{DOWN}{DOWN}{RIGHT}{DOWN}")
;EndFunc

Func fnGen2012and13()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   
   Send("{RIGHT}10{RIGHT}2012")
   Sleep(100)
   
     ; open calendar
   MouseClick("left", 488, 271)
   
   ; move calendar to december
   ; UPDATED 9 Sept 2013
   ; ===== CHANGE THIS
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   
   ; click on 31
   MouseClick("left", 451, 437)
   
   ;Send("{ENTER}")
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   
   MouseMove(412, 77)
EndFunc

Func fnGen2013()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   
   Send("{RIGHT}01{RIGHT}")
   Sleep(500)
   Send("{ENTER}")
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func fnGen2012()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   
   Send("{RIGHT}01{RIGHT}2012")
   Sleep(100)

   ; open calendar
   MouseClick("left", 488, 271)
   
   ; move calendar to december
   ; UPDATED 9 Sept 2013
   ; ===== CHANGE THIS
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   
   ; click on 31
   MouseClick("left", 451, 437)
   
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func CLOSEClicked()
   Exit
EndFunc