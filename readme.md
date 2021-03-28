# btps.motd

Message of the Day (motd).

## Pré-requis

Afin de fonctionner avec SSH, la directive UsePam de SSH doit être à "Yes" car c'est Pam qui génère le fichier /run/motd.dynamic lors de la connexion de l'utilisateur.

Pour ne pas voir le motd 3 fois :
- Dans /etc/ssh/sshd_config, mettre "PrintMotd" à "No" (car c'est Pam qui va l'afficher)
- Dans /etc/pam.d/sshd, commenter "session    optional     pam_motd.so  motd=/run/motd.dynamic"
- Celui qui fait le boulot est dans /etc/pam.d/login

## Variables du role

Aucune variable.

## Dépendances de ce role

Aucune dépendance.

## Exemple d'utilisation

Dans le playbook :
```yaml
---
- hosts: all
  roles:
    - btps.motd

```

## Compatibilités

Ce role fonctionne sur Debian 9.

## Notes

Documentations utilisées à la résolution de problématiques :
- https://doc.ubuntu-fr.org/motd
- https://nickcharlton.net/posts/debian-ubuntu-dynamic-motd.html
- https://stackoverflow.com/questions/190912/etc-motd-printing-twice-on-gentoo-linux

## Todo

- Le script 00-alteo comporte le test suivant qui ne devrait plus fonctionner car le compte root n'est plus utilisé pour la maintenance.
```bash
if [ -e /root/file ]
then
	echo $R"========================================================"
	echo "=              Serveur bloque pour impaye              ="
	echo "========================================================"
	echo $RESET
fi
```

- Retravailler le script motd "file/etc/update-motd.d/00-alteo" (spliter en plusieurs scripts ? cf. https://doc.ubuntu-fr.org/motd)
- Ajouter un lien vers la FAQ Alteo.
- Faire fonctionner sur Centos 7
