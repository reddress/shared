;; Alterations for Italian
;; Remove slash (/) combinations

;; Create a lisp/ directory under emacs-VERSION/
;; Place this file in the lisp/ directory and byte-compile it

;; Add to ~/.emacs

;; custom italian input method
;; (add-to-list 'load-path "c:/Users/neo/Desktop/emacs27/lisp/")
;; (require 'italian)

;; ;; optional
;; (setq default-input-method "italian-prefix")



;;; latin-pre.el --- Quail packages for inputting various European characters  -*-coding: utf-8;-*-

;; Copyright (C) 1997-2017 Free Software Foundation, Inc.
;; Copyright (C) 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
;;   2006, 2007, 2008, 2009, 2010, 2011
;;   National Institute of Advanced Industrial Science and Technology (AIST)
;;   Registration Number H14PRO021

;; Keywords: mule, multilingual, latin, input method

;; This file is part of GNU Emacs.

;; GNU Emacs is free software: you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation, either version 3 of the License, or
;; (at your option) any later version.

;; GNU Emacs is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.

;; You should have received a copy of the GNU General Public License
;; along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.

;;; Commentary:

;; Key translation maps were originally copied from iso-acc.el.
;; latin-1-prefix: extra special characters added, adapted from the vim
;;                 digraphs (from J.H.M.Dassen <jdassen@wi.leidenuniv.nl>)
;;                 by R.F. Smith <rsmith@xs4all.nl>
;;
;; polish-slash:
;; Author: Włodek Bzyl <matwb@univ.gda.pl>
;; Maintainer: Włodek Bzyl <matwb@univ.gda.pl>
;;
;; latin-[89]-prefix: Dave Love <fx@gnu.org>

;; You might make extra input sequences on the basis of the X
;; locale/*/Compose files (which have both prefix and postfix
;; sequences), but bear in mind that sequences which are logical in
;; that context may not be sensible when they're not signaled with
;; the Compose key.  An example is a double space for NBSP.

;;; Code:

(require 'quail)

(quail-define-package
 "italian-prefix" "Italian-1" "IT" t
 "Latin-1 characters input method with prefix modifiers

    effect   | prefix | examples
 ------------+--------+----------
    acute    |   \\='    | \\='a -> á, \\='\\=' -> ´
    grave    |   \\=`    | \\=`a -> à
  circumflex |   ^    | ^a -> â
  diaeresis  |   \"    | \"a -> ä  \"\" -> ¨
    tilde    |   ~    | ~a -> ã
   cedilla   |   ~    | ~c -> ç
    misc     | \" ~ /  | \"s -> ß  ~d -> ð  ~t -> þ  /a -> å  /e -> æ  /o -> ø
   symbol    |   ~    | ~> -> »  ~< -> «  ~! -> ¡  ~? -> ¿  ~~ -> ¸
             |   ~    | ~s -> §  ~x -> ¤  ~. -> ·  ~$ -> £  ~u -> µ
             |   ~    | ~p -> ¶  ~- -> ­  ~= -> ¯  ~| -> ¦
   symbol    |  _ /   | _o -> º  _a -> ª  // -> °  /\\ -> ×  _y -> ¥
             |  _ /   | _: -> ÷  /c -> ¢  /2 -> ½  /4 -> ¼  /3 -> ¾
             |  _ /   | /= -> ¬
   symbol    |   ^    | ^r -> ®  ^c -> ©  ^1 -> ¹  ^2 -> ²  ^3 -> ³
" nil t nil nil nil nil nil nil nil nil t)

(quail-define-rules
 ("'A" ?Á)
 ("'E" ?É)
 ("'I" ?Í)
 ("'O" ?Ó)
 ("'U" ?Ú)
 ("'a" ?á)
 ("'e" ?é)
 ("'i" ?í)
 ("'o" ?ó)
 ("'u" ?ú)
 ("''" ?')
 ("' " ?')
 ("`A" ?À)
 ("`E" ?È)
 ("`I" ?Ì)
 ("`O" ?Ò)
 ("`U" ?Ù)
 ("`a" ?à)
 ("`e" ?è)
 ("`i" ?ì)
 ("`o" ?ò)
 ("`u" ?ù)
 ("``" ?`)
 ("` " ?`)
 ("^A" ?Â)
 ("^E" ?Ê)
 ("^I" ?Î)
 ("^O" ?Ô)
 ("^U" ?Û)
 ("^a" ?â)
 ("^e" ?ê)
 ("^i" ?î)
 ("^o" ?ô)
 ("^u" ?û)
 ("^^" ?^)
 ("^ " ?^)
 ("\"A" ?Ä)
 ("\"E" ?Ë)
 ("\"I" ?Ï)
 ("\"O" ?Ö)
 ("\"U" ?Ü)
 ("\"a" ?ä)
 ("\"e" ?ë)
 ("\"i" ?ï)
 ("\"o" ?ö)
 ("\"s" ?ß)
 ("\"u" ?ü)
 ("\"y" ?ÿ)
 ("\"\"" ?¨)
 ("\" " ?\")
 ("~A" ?Ã)
 ("~C" ?Ç)
 ("~D" ?Ð)
 ("~N" ?Ñ)
 ("~O" ?Õ)
 ("~T" ?Þ)
 ("~a" ?ã)
 ("~c" ?ç)
 ("~d" ?ð)
 ("~n" ?ñ)
 ("~o" ?õ)
 ("~t" ?þ)
 ("~>" ?\»)
 ("~<" ?\«)
 ("~!" ?¡)
 ("~?" ?¿)
 ("~~" ?¸)
 ("~ " ?~)
 ("_o" ?º)
 ("_a" ?ª)
 ("_ " ? )
 ("^1" ?¹)
 ("^2" ?²)
 ("^3" ?³)
 ("~-" ?­)
 ("~|" ?¦)
 ("~=" ?¯)
 )

(provide 'italian)
