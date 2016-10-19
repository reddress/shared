#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Global $verif = FileOpen("sorted.txt", 0)

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Cardex Verif", 600, 120, 0, 580)
WinSetOnTop("Cardex Verif", "", 1)

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
;$mylabel = GUICtrlCreateLabel("Version: May (update in June)", 30, 10)
$codigo = GUICtrlCreateInput("", 20, 10, 66, 19)

$button2012 = GUICtrlCreateButton("2012", 20, 40, 60)
$button2013 = GUICtrlCreateButton("2013", 90, 40, 60)
;; REMOVE LATER
;;GUICtrlSetState(-1, $GUI_DISABLE)
$button2012and13 = GUICtrlCreateButton("now-Mar.8", 40, 70, 85)

$estoque = GUICtrlCreateInput("", 92, 10, 110, 19)
;;$notes = GUICtrlCreateEdit("Último container - saldo anterior", 208, 10, 348, 100)
$notes = GUICtrlCreateEdit("", 208, 10, 348, 100)

$buttonNext = GUICtrlCreateButton("next", 166, 40)
$buttonClip = GUICtrlCreateButton("copy", 166, 70)
$buttonClear = GUICtrlCreateButton("clear", 562, 10)
$buttonLoad = GUICtrlCreateButton("load", 5, 75)
;$buttonAddUC = GUICtrlCreateButton("add UC", 550, 40)



GUICtrlSetOnEvent($button2012, "fnGen2012")
GUICtrlSetOnEvent($button2013, "fnGen2013")
GUICtrlSetOnEvent($button2012and13, "fnGen2012and13")
GUICtrlSetOnEvent($buttonNext, "fnNext")
GUICtrlSetOnEvent($buttonClear, "fnClearEdit")
GUICtrlSetOnEvent($buttonClip, "fnCopyToClipboard")
GUICtrlSetOnEvent($buttonLoad, "fnLoad")

;GUICtrlSetOnEvent($buttonAddUC, "addUC")

;$estoque = GUICtrlCreateEdit("", 172, 10, 70, 50, BitOR($ES_AUTOVSCROLL, $ES_AUTOHSCROLL, $ES_WANTRETURN))
GUISetState(@SW_SHOW)
$oldcode = ""

While 1
   $newcode = GUICtrlRead($codigo)
   If $oldcode <> $newcode Then
	  GUICtrlSetData($notes, "Último container - saldo anterior")
	  GUICtrlSetData($notes, "")
	  GUICtrlSetData($estoque, "")
	  $oldcode = $newcode
   EndIf
   Sleep(100)
WEnd

Func fnNext()
   Local $line = FileReadLine($verif)
   If @error = -1 Then
	  GUICtrlSetData($codigo, "END")
   Else
	  GUICtrlSetData($codigo, $line)
   EndIf
EndFunc

Func fnClearEdit()
   GUICtrlSetData($notes, "")
   GUICtrlSetData($codigo, "")
EndFunc

Func addUC()
   GUICtrlSetData($notes, GUICtrlRead($notes) & @CRLF & "Último container - saldo anterior")
   GUICtrlSetData($notes, "")
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

Func fnLoad()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   MouseMove(20, 687)
EndFunc

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
   
   Send("21{RIGHT}10{RIGHT}2012")
   Sleep(100)
   
     ; open calendar
   MouseClick("left", 488, 271)
   
   ; move calendar to march 2012
   ; UPDATED 21 oct 2013
   ; ===== CHANGE THIS
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   
   ; click on 7
   MouseClick("left", 548, 364)
   
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