(require 'package);;加载包管理器
;;设置插件源
(setq package-archives '(("gnu" . "http://elpa.emacs-china.org/gnu/")
                          ("melpa" . "http://elpa.emacs-china.org/melpa/")))
;;(add-to-list 'package-archives
;;             '("marmalade" . "http://marmalade-repo.org/packages/"))
(package-initialize);;初始化包

(global-linum-mode 1) ;;1表示行号常显
(setq linum-format "%d ");;注意%d后有空格，即用空格将行号和代码隔开。

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-safe-themes
   (quote
    ("0598c6a29e13e7112cfbc2f523e31927ab7dce56ebb2016b567e1eff6dc1fd4f" default)))
 '(package-selected-packages (quote (solarized-theme elpy))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
)

;; Configuration of Python IDE  
;; https://github.com/jorgenschaefer/elpy  
(require 'elpy nil t)  
(elpy-enable) 
;; enable elpy jedi backend
(setq elpy-rpc-backend "jedi")
;;(setq elpy-rpc-python-command "python3")  ;; python3
(setq python-shell-interpreter "/home/he/.local/bin/ipython")
python-shell-interpreter-args “–profile=dev” )

;; Fixing a key binding bug in elpy
(define-key yas-minor-mode-map (kbd "C-c k") 'yas-expand)
;; Fixing another key binding bug in iedit mode
(define-key global-map (kbd "C-c o") 'iedit-mode)

;;for use jupyter ,install ein(emacs ipython notebook)

