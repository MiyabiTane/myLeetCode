;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

;; ALEXNOTE:  this is very interesting, I think it's cool that you write it in a lisp-like language
;;            and that it performs so much better than the Python version.
;;            Question: do you know if this code runs compiled or interpreted? Maybe that explains the large difference.
;; Tanemoto : I think this code runs interpreted.

(ros::roseus "hello")

(defun calc_mat (n)
  ;; prepare matrix a, b
  (setq a '())
  (setq b '())
  (dotimes (i n)
    (setq sub_a '())
    (setq sub_b '())
    (dotimes (j n)
      (setq sub_a (append sub_a (list (+ (* i n) j))))
      (setq sub_b (append sub_b (list (+ (* j n) i))))
      )
    (setq a (list-insert sub_a (+ i 1) a))
    (setq b (list-insert sub_b (+ i 1) b))
    )
  ;;(format t "a is ~A~%" a)
  ;;(format t "b is ~A~%" b)
  
  ;;calculate mal of a, b
  ;;elt localtime 0 -> 
  ;;(setq start_time (unix:localtime))
  (format t "~A : START ~Asec~%" n (ros::time-now))
  (setq c '())
  (dotimes (i n)
    (setq sub_c '())
    (dotimes (j n)
      (setq num_c 0)
      (dotimes (k n)
	(setq num_a (elt (elt a i) k))
	(setq num_b (elt (elt b k) j))
	(setq num_c (+ num_c (* num_a num_b)))
	)
      (setq sub_c (append sub_c (list num_c)))
      )
    (setq c (list-insert sub_c (+ i 1) c))
    )
  (format t "~A : END ~Asec~%" n (ros::time-now))
  ;;(format t "c is ~A~%" c)
  
  
  ;;calculate sum
  (setq total 0)
  (dotimes (i n)
    (dotimes (j n)
      (setq total (+ total (elt (elt c i) j)))
      )
    )
  ;;(format t "total is ~A~%" total)
  )

(defun main ()
  (dotimes (i 81)
    (calc_mat i)
    )
  )

(main)
