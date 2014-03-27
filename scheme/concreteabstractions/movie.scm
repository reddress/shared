;; This file contains excerpts from the textbook Concrete
;; Abstractions: An Introduction to Computer Science Using Scheme, by
;; Max Hailperin, Barbara Kaiser, and Karl Knight, Copyright (c) 1998
;; by the authors. Full text is available for free at
;; http://www.gustavus.edu/+max/concrete-abstractions.html
;;
;; Revision 1.3 as of 2005/12/20 14:09:37

;; Chapter 7: Lists

;; 7.3  Basic List Processing Techniques

(define filter
  (lambda (ok? lst)
    (cond ((null? lst)
           '())
          ((ok? (car lst))
           (cons (car lst) (filter ok? (cdr lst))))
          (else
           (filter ok? (cdr lst))))))

;; 7.6  An Application: A Movie Query System

(define make-movie
  (lambda (title director year-made actors)
    (list title director year-made actors)))

(define movie-title car)
(define movie-director cadr)
(define movie-year-made caddr)
(define movie-actors cadddr)

(define our-movie-database   ;; longer version than in the text
  (list (make-movie '(amarcord)
                    '(federico fellini)
                    1974
                    '((magali noel) (bruno zanin)
                                    (pupella maggio)
                                    (armando drancia)))
        (make-movie '(the big easy)
                    '(jim mcbride)
                    1987
                    '((dennis quaid) (ellen barkin)
                                     (ned beatty)
                                     (lisa jane persky)
                                     (john goodman)
                                     (charles ludlam)))
        (make-movie '(boyz n the hood)
                    '(john singleton)
                    1991
                    '((cuba gooding jr.) (ice cube)
                                         (larry fishburne)
                                         (tyra ferrell)
                                         (morris chestnut)))
        (make-movie '(dead again)
                    '(kenneth branagh)
                    1991
                    '((kenneth branagh) (emma thompson)
                                        (andy garcia)
                                        (derek jacobi)
                                        (hanna schygulla)))
        (make-movie '(the godfather)
                    '(francis ford coppola)
                    1972
                    '((marlon brando) (al pacino)
                                      (james caan)
                                      (robert duvall)
                                      (diane keaton)))
        (make-movie '(an american in paris)
                    '(vincente minnelli)
                    1952
                    '((gene kelley) (leslie caron)
                                    (oscar levant)
                                    (nina foch)
                                    (george guetary)))
        (make-movie '(casablanca)
                    '(michael curtiz)
                    1942
                    '((humphrey bogart) (ingrid bergman)
                                        (paul henreid)
                                        (claude rains)
                                        (sydney greenstreet)
                                        (peter lorre)
                                        (s z sakall)
                                        (conrad veidt)
                                        (dooley wilson)))
        (make-movie '(citizen kane)
                    '(orson welles)
                    1941
                    '((orson welles) (joseph cotten)
                                     (dorothy comingore)
                                     (ray collins)
                                     (george coulouris)
                                     (agnes moorehead)
                                     (ruth warrick)))
        (make-movie '(gone with the wind)
                    '(victor fleming)
                    1939
                    '((clark gable) (vivien leigh)
                                    (leslie howard)
                                    (olivia de havilland)
                                    (hattie mcdaniel)
                                    (butterfly mcqueen)))
        (make-movie '(lawrence of arabia)
                    '(david lean)
                    1962
                    '((peter otoole) (alec guinness)
                                     (anthony quinn)
                                     (jack hawkins)
                                     (jose ferrer)
                                     (omar sharif)
                                     (anthony quayle)
                                     (claude rains)
                                     (arthur kennedy)
                                     (donald wolfit)))
        (make-movie '(the manchurian candidate)
                    '(john frankenheimer)
                    1962
                    '((frank sinatra) (laurence harvey)
                                      (janet leigh)
                                      (angela lansbury)
                                      (henry silva)
                                      (james gregory)
                                      (leslie parrish)
                                      (john mcgiver)
                                      (khigh dhiegh)
                                      (james edwards)))
        (make-movie '(metropolis)
                    '(fritz lang)
                    1926
                    '((alfred abel) (gustay frohlich)
                                    (brigitte helm)
                                    (rudolf kleinrogge)
                                    (heinrich george)))
        (make-movie '(othello)
                    '(orson welles)
                    1952
                    '((orson welles) (michael mac liammoir)
                                     (robert coote)
                                     (suzanne cloutier)
                                     (faye compton)
                                     (doris dowling)
                                     (michael laurence)))
        (make-movie '(spartacus)
                    '(stanley kubrick)
                    1960
                    '((kirk douglas) (laurence olivier)
                                     (jean simmons)
                                     (charles laughton)
                                     (peter ustinov)
                                     (john gavin)
                                     (tony curtis)
                                     (woody strode)))
        (make-movie '(a star is born)
                    '(george cuckor)
                    1954
                    '((judy garland) (james mason)
                                     (jack carson)
                                     (tommy noonan)
                                     (charles bickford)))
        (make-movie '(after the rehearsal)
                    '(ingmar bergman)
                    1984
                    '((erland josephson) (ingrid thulin)
                                         (lena olin)
                                         (nadja palmstjerna-weiss)))
        (make-movie '(amadeus)
                    '(milos forman)
                    1984
                    '((f murray abraham) (tom hulce)
                                         (elizabeth berridge)
                                         (simon callow)
                                         (roy dotrice)
                                         (christine ebersole)
                                         (jeffrey jones)))
        (make-movie '(blood simple)
                    '(joel coen)
                    1985
                    '((john getz) (frances mcdormand)
                                  (dan hedaya)
                                  (m emmet walsh)
                                  (samm-art williams)))
        (make-movie '(chinatown)
                    '(roman polanski)
                    1974
                    '((jack nicholson) (faye dunaway)
                                       (john huston)
                                       (perry lopez)
                                       (john hillerman)
                                       (darrell zwerling)
                                       (diane ladd)
                                       (roman polanski)))
        (make-movie '(the cotton club)
                    '(francis ford coppola)
                    1984
                    '((richard gere) (gregory hines)
                                     (diane lane)
                                     (lonette mckee)
                                     (bob hoskins)
                                     (james remar)
                                     (fred gwynne)))
        (make-movie '(the crying game)
                    '(neil jordan)
                    1992
                    '((stephen rea) (jaye davidson)
                                    (forest whitaker)
                                    (miranda richardson)
                                    (adrian dunbar)
                                    (breffini mckenna)
                                    (joe savino)))
        (make-movie '(the day of the jackal)
                    '(fred zinnemann)
                    1973
                    '((edward fox) (terence alexander)
                                   (michel auclair)
                                   (alan badel)
                                   (tony britton)
                                   (denis carey)
                                   (olga georges-picot)
                                   (cyril cusack)))
        (make-movie '(diva)
                    '(jean-jacques beineix)
                    1981
                    '((wilhelmenia wiggins fernandez)
                      (frederic andrei)
                      (richard bohringer)
                      (thay an luu)
                      (jacques fabbri)
                      (chantal deruaz)))
        (make-movie '(the dresser)
                    '(peter yates)
                    1984
                    '((albert finney) (tom courtenay)
                                      (edward fox)
                                      (zena walker)))
        (make-movie '(el norte)
                    '(gregory nava)
                    1983
                    '((zaide silvia gutierrez) (david villalpando)
                                               (ernesto gomez cruz)
                                               (alicia del lago)
                                               (trinidad silva)))
        (make-movie '(the exorcist)
                    '(william friedkin)
                    1973
                    '((ellen burstyn) (linda blair)
                                      (jason miller)
                                      (max von sydow)
                                      (kitty winn)
                                      (lee j cobb)))
        (make-movie '(a fish called wanda)
                    '(michael chrichton)
                    1988
                    '((john cleese) (jamie lee curtis)
                                    (kevin kline)
                                    (michael palin)
                                    (maria aitken)
                                    (tom georgeson)
                                    (patricia hayes)))
        (make-movie '(flirting)
                    '(john duigan)
                    1992
                    '((noah taylor) (thandie newton)
                                    (nicole kidman)
                                    (bartholomew rose)
                                    (felix nobis)
                                    (josh picker)
                                    (kiri paramore)))
        (make-movie '(gates of heaven)
                    '(errol morris)
                    1978
                    '())
        (make-movie '(house of games)
                    '(david mamet)
                    1987
                    '((lindsay crouse) (joe mantegna)
                                       (mike nussman)
                                       (lilia skala)
                                       (j t walsh)
                                       (jack wallace)))
        (make-movie '(iceman)
                    '(fred schepisi)
                    1984
                    '((timothy hutton) (john lone)
                                       (lindsay crouse)))
        (make-movie '(jaws)
                    '(steven spielberg)
                    1975
                    '((roy scheider) (robert shaw)
                                     (richard dreyfuss)
                                     (lorraine gary)
                                     (murray hamilton)))
        (make-movie '(johnny got his gun)
                    '(dalton trumbo)
                    1971
                    '((timothy bottoms) (kathy fields)
                                        (jason robards)
                                        (diane varsi)
                                        (donald sutherland)
                                        (eduard franz)))
        (make-movie '(local hero)
                    '(bill forsyth)
                    1983
                    '((burt lancaster) (peter reigert)
                                       (peter capaldi)
                                       (fulton mckay)
                                       (denis lawson)))
        (make-movie '(malcolm x)
                    '(spike lee)
                    1992
                    '((denzel washington) (angela basset)
                                          (albert hall)
                                          (al freeman jr)
                                          (delroy lindo)
                                          (spike lee)))))

;; Note that before you can use query-loop, you will need to
;; write substitutions-in-to-match and movies-satisfying.

(define query-loop
  (lambda ()
    (newline)
    (newline)
    (let ((query (read)))
      (cond ((exit? query) (display '(see you later)))
            ;; movie-p/a-list is the list of the
            ;;  pattern/action pairs
            (else (answer-by-pattern query movie-p/a-list)
                  (query-loop))))))

(define exit?
  (lambda (query)
    (member query '((bye)
                    (quit)
                    (exit)
                    (so long)
                    (farewell)))))

(define answer-by-pattern
  (lambda (query p/a-list)
    (cond ((null? p/a-list)
           (display '(i do not understand)))
          ((matches? (pattern (car p/a-list)) query)
           (let ((subs (substitutions-in-to-match
                        (pattern (car p/a-list))
                        query)))
             (let ((result (apply (action (car p/a-list))
                                  subs)))
               (if (null? result)
                   (display '(i do not know))
                   (display result)))))
          (else
           (answer-by-pattern query
                              (cdr p/a-list))))))

(define make-pattern/action
  (lambda (pattern action)
    (cons pattern action)))

(define pattern car)
(define action cdr)

;; The following definition of move-p/a-list is the first one given in
;; the text. The second version is later in this file, but commented
;; out with semicolons.  To use it, delete the semicolons.  In either
;; case, you are expected to add to the list.

(define movie-p/a-list
  (list (make-pattern/action
         '(who is the director of ...)
         (lambda (title)
           (movies-satisfying 
            our-movie-database
            (lambda (movie) (equal? (movie-title movie) title))
            movie-director)))))

;; The following definition of matches? is the first one given
;; in the text. The second version is later in this file, but commented
;; out with semicolons.  To use it, delete the semicolons.

(define matches?
  (lambda (pattern question)
    (cond ((null? pattern)  (null? question))
          ((null? question) #f)
          ((equal? (car pattern) '...) #t)
          ((equal? (car pattern) (car question))
           (matches? (cdr pattern)
                     (cdr question)))
          (else #f))))

;; The following definition of matches? is the second one given in the
;; text. The first version is eariler in this file. To use this second
;; version, delete the semicolons.  You are also expected to further
;; extend this version.

;(define matches?
;  (lambda (pattern question)
;    (cond ((null? pattern)  (null? question))
;          ((null? question) #f)
;          ((list? (car pattern))
;           (if (member (car question) (car pattern))
;               (matches? (cdr pattern)
;                         (cdr question))
;               #f))
;          ((equal? (car pattern) '...) #t)
;          ((equal? (car pattern) (car question))
;           (matches? (cdr pattern)
;                     (cdr question)))
;          (else #f))))

;; The following definition of movie-p/a-list is the second one given in the
;; text. The first version is eariler in this file. To use this second
;; version, delete the semicolons.  To use it, you first need to write
;; the-only-element-in.  You are also expected to add more to this
;; list.

;(define movie-p/a-list
;  (list (make-pattern/action
;         '(who is the director of ...)
;         (lambda (title)
;           (the-only-element-in
;            (movies-satisfying 
;             our-movie-database
;             (lambda (movie) (equal? (movie-title movie) title))
;             movie-director))))
;        (make-pattern/action
;         '(what (movie movies) (was were) made in _)
;         (lambda (noun verb year)
;           (movies-satisfying 
;            our-movie-database
;            (lambda (movie) (= (movie-year-made movie) year))
;            movie-title)))))
