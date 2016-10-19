#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Global $verif = FileOpen("sortedautoit.txt", 0)

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Cardex Verif", 600, 120, 0, 580)
WinSetOnTop("Cardex Verif", "", 1)

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
;$mylabel = GUICtrlCreateLabel("Version: May (update in June)", 30, 10)
$codigo = GUICtrlCreateInput("", 20, 10, 56, 19)

$button2014 = GUICtrlCreateButton("2014", 20, 40, 60)
$button2013 = GUICtrlCreateButton("2013", 90, 40, 60)
;; REMOVE LATER
;;GUICtrlSetState(-1, $GUI_DISABLE)
$button2012and13 = GUICtrlCreateButton("now-Mar.8", 40, 70, 85)

$estoque = GUICtrlCreateInput("", 159, 10, 45, 19)
$estoque2 = GUICtrlCreateInput("", 159, 35, 45, 19)
$japediu = GUICtrlCreateInput("", 82, 10, 75, 19) 
$notes = GUICtrlCreateEdit("Último container - saldo anterior", 208, 10, 348, 100)
;;$notes = GUICtrlCreateEdit("", 208, 10, 348, 100)

$buttonNext = GUICtrlCreateButton("next", 166, 60)
$buttonClip = GUICtrlCreateButton("copy", 166, 90)
$buttonClear = GUICtrlCreateButton("clear", 562, 10)
$buttonLoad = GUICtrlCreateButton("load", 5, 75)
;$buttonAddUC = GUICtrlCreateButton("add UC", 550, 40)



GUICtrlSetOnEvent($button2014, "fnGen2014")
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
	;;  GUICtrlSetData($notes, "")
	  GUICtrlSetData($estoque, "")
	  GUICtrlSetData($estoque2, "")
	  $oldcode = $newcode
   EndIf
   Sleep(100)
WEnd

Func fnNext()
   Local $line = FileReadLine($verif)
   If @error = -1 Then
	  GUICtrlSetData($codigo, "END")
   Else
	  If StringInStr($line, "@") Then
		 Local $chegando = StringSplit($line, "@")
		 GUICtrlSetData($japediu, $chegando[2])
		 GUICtrlSetData($codigo, $chegando[1])
	  Else
		 GUICtrlSetData($japediu, "")
		 GUICtrlSetData($codigo, $line)
	  EndIf
   EndIf
   
   ; manipulate Python Gui
   MouseClick("left", 770, 610)
   MouseClick("left", 870, 610)
   Send(GUICtrlRead($codigo))
   MouseClick("left", 975, 610)
   
   ; click on fnNext()
   MouseClick("left", 20, 690)
EndFunc

Func fnClearEdit()
   GUICtrlSetData($notes, "")
   GUICtrlSetData($codigo, "")
EndFunc

Func addUC()
   GUICtrlSetData($notes, GUICtrlRead($notes) & @CRLF & "Último container - saldo anterior")
   ;;GUICtrlSetData($notes, "")
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
   MouseMove(180, 669)
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
   Sleep(600)
   
   Send("{RIGHT}01{RIGHT}2013")
   Sleep(200)
   ;; Send("{ENTER}")
   ;
   Sleep(100)

   ; open calendar
   MouseClick("left", 488, 271)
   
   ; move calendar to december
   ; UPDATED 6 mar 2014
   ; ===== CHANGE THIS
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   
   ; click on 31
   MouseClick("left", 484, 438)
   
   Sleep(100)
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func fnGen2014()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(600)
   
   Send("{RIGHT}01{RIGHT}2014")
   Sleep(100)
   
   Send("{ENTER}")

   ; open calendar
   ; MouseClick("left", 488, 271)
   
   ; move calendar to december
   ; UPDATED 9 Sept 2013
   ; ===== CHANGE THIS
   ; MouseClick("left", 414, 297)
   ; MouseClick("left", 414, 297)
   ; ...etc... 
   
   ; click on 31
   ; MouseClick("left", 451, 437)
   
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func CLOSEClicked()
   Exit
EndFunc