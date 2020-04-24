# Semaine de Formation du 20 au 24 avril 2020 - M2-IOT  

_______________

# Au programme 🤖

* Lundi 20 avril :
	* Rapels python POO
	* Rapels librairies numpy et pandas 
  
* Mardi 21 avril : 
	* Rapels librairies numpy, pandas et sklearn (suite)
	* Workshop Docker et python 
  
* Mercredi 22 avril : 
	* Workshop Docker (suite)
	* Workshop API python 

* Jeudi 23 avril : 
	* Workshop flask pour le ml 

* Vendredi 24 avril :   
	* Workshop flask pour le ml (suite)


_______________



## Suivi 📈

Créer un repo github et faire a minima deux pushs par jour (matin et aprem) afin que je vois ou vous en êtes 👌


## Rappels python POO 👨‍🎓

### Vos missions 

Sur le drive pour les consignes dossier python [ici](https://drive.google.com/drive/folders/1EnDYGM5SvIFbzrEHHAG8lN-l4Lwe9851?usp=sharing)


## Rappels data visualisation numpy & pandas 📊


### Vos missions 

Sur le drive pour les consignes dossier dataviz et les data dossier data [ici](https://drive.google.com/drive/folders/1EnDYGM5SvIFbzrEHHAG8lN-l4Lwe9851?usp=sharing)

## Workshop Docker et python 🐳


Docker est un logiciel libre permettant de lancer des applications dans des conteneurs logiciels.
Il ne s'agit pas de virtualisation, mais de conteneurisation, une forme plus légère qui s'appuie sur certaines parties de la machine hôte pour son fonctionnement. Cette approche permet d'accroître la flexibilité et la portabilité d’exécution d'une application, laquelle va pouvoir tourner de façon fiable et prévisible sur une grande variété de machines hôtes, que ce soit sur la machine locale, un cloud privé ou public, etc. Plus d'information sur la documentation officielle [ici](https://docs.docker.com/v17.09/). 

Docker a été inventé pour résoudre un probleme classique que nous avons tous rencontré en informatique. 
Un meme parle toujours mieux que milles mots : 
<div style="text-align:center">
<img src="https://external-preview.redd.it/aR6WdUcsrEgld5xUlglgKX_0sC_NlryCPTXIHk5qdu8.jpg?auto=webp&s=5fe64dd318eec71711d87805d43def2765dd83cd">
</div>


### Vos missions 

**Quickstart** 

* comprendre la différence entre images et containers et à quoi sert un `Dockerfile` 
* installer docker sur votre machine (Ubuntu de préférence) 
* lancer votre premier container ubuntu, l'équivalent du *hello-world* de docker  
* regarder si votre container est bien lancer 
* faire un résumé type `cheat sheet` des principales commandes dockers relatives aux images et containers 
* vérifier en vous connectant à votre container qu'il est bien `up` et qu'il s'aggit bien 
* créer un repo github pour les deux jours  ⚠️avec un README.md explicite svp⚠️
* faire un push de votre travail sur votre repo et m'envoyer le lien. 

**DS Sand box container**

* coder un container type *data engineering sandbox* à partir d'une image Ubuntu    contenant : 
	* un espace de travail appelé workspace 
	* python3, pip3 et vim 
	* une installation automatique du fichier `requirements.txt`
	* un set up des credentials git pour l'utilisateur du container
	* une exposition du port 8000 
	* pour finir le container devra lancer jupyter notebook avec votre git clonné à la racine  
* faire un push de votre travail sur votre repo. 
* faire un résumé type *cheat sheet* des principales commandes des `Dockerfile`
* expliquer à quoi sert la commance ci-dessous 

#### Une commande qui peut vous servir   
```bash
$ sudo groupadd docker
$ sudo gpasswd -a $USER docker
```


## Workshop API python 🛰

Une API (Application Programmable Interface) est un ensemble de fonctions permettant à une application d'offrir des services à d'autres logiciels. Une API peut être distribué localement dans un programme informatique ou au contraire peut avoir vocation a être utilisée par un plus grand nombre d'acteurs.

Dans ce cours nous nous intéressons surtout au API Web, c'est-à-dire celles qui permettent de fournir une interface accessible en ligne. Cela est le cas lorsque l'on effectue une requête à un serveur afin que l'on reçoive le résultat d'un traitement. 

### REST

L'architecture REST est, depuis $10$ ans, une des architectures les plus utilisées. En effet, elle est rapide a mettre en place, extrêmement puissante et répond à une très large majorité des cas. Par exemple, supposons que l'on souhaite un ensemble de programmes (site Web, application Smartphone) permettant de réserver et de gérer ses vols d'avions. Une architecture REST pourrait centraliser les fonctionnalités comme le montre le diagramme suivant.

![Exemple d'architecture REST](https://i.ytimg.com/vi/UQwjytQzoqE/maxresdefault.jpg)


### Routes

Les requêtes HTTP se caractérisent par des **routes** : il s'agit d'un chemin permettant de structurer l'accessibilité des opérations. Reprenons l'exemple de gestion de vols d'avions :
- la route http://monserveur.com/list permet de lister les vols disponibles
- la route http://monserveur.com/fly permet d'ajouter ou modifier un vol
- la route http://monserveur.com/action/disconnect permet de déconnecter l'utilisateur
Cette structuration permet ainsi d'organiser toutes les fonctionnalités disponibles via l'API de manière cohérente et ergonomique. Les routes *list*, *fly* et *action/disconnect* sont donc définies par l'architecte logiciel dans le code de l'API.

### Les verbes HTTP

La philosophie de l'architecture REST est de proposer une route permettant d'effectuer un traitement en rapport avec une action précise. Par exemple, la route *fly* permet d'ajouter ou modifier un vol, mais comment spécifie-t-on précisement si l'on souhaite ajouter, modifier ou supprimer un vol ? C'est ainsi que les verbes HTTP ont été conçus pour faciliter cette interaction :

- **GET** effectue une lecture
- **POST** crée une donnée
- **PUT** met à jour une donnée
- **DELETE** supprime une donnée

#### Les codes 

Lorsque l'on effectue une requête, un code HTTP est automatiquement fourni. Ce code permet d'identifier le résultat d'une requête ou d'indiquer une éventuelle erreur lors du traitement d'une requête. Les plus connues sont :
- 200 : Succès
- 400 : Erreur de syntaxe
- 404 : Introuvable
- 403 : Interdit
- 500 : Erreur interne
Lorsque l'on code une API REST, il est fortement conseillé de fournir des codes HTTP spécifiques pour informer les utilisateurs de l'état d'une requête.

Plus d'informations [ici](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀


### Vos missions 

* se renseigner sur les API de façon générale et à quoi cela sert, quel interet peut avoir une entreprise à développer des services API
* se renseigner sur flask et faire une petite application qui renvoie `hello word`, expliquer ce qu'est une route 
* charger le ficher `book.json` dans votre application et créer une route `/books` qui renvoie ce fichier 
* ajouter une route qui renvoie un certain livre 
* faire un push de votre travail sur votre repo
* écrire un `Dockerfile` pour votre application
* builder votre image et lancer un container   
* verifier que votre container est bien actif avec les commandes docker 
* faire un fichier `test_api.sh` pour tester votre api
* faire un push de votre travail sur votre repo


## Workshop flask pour le ml 🚀


### Vos mission

* se renseigner sur le déploiement de modèle de ML
* ecrire un algorithme pour classer les données du fichier labels.csv et le deployer avec flask. 



## Les ressources utiles 👀

### Les bases en rapide
- python doctor : https://python.doctor
- glossaire ml/ia : https://developers.google.com/machine-learning/glossary 
- Cheat sheet ml/ia : https://ml-cheatsheet.readthedocs.io/en/latest/


### Pour les api 
- flask doc : https://palletsprojects.com/p/flask/
- flask ml app in 5min : https://www.kdnuggets.com/2019/01/build-api-machine-learning-model-using-flask.html 
- flask app example (boston houses project) : https://hackernoon.com/machine-learning-w22g322x 
- flask-restful doc : https://flask-restful.readthedocs.io/en/latest/quickstart.html


### Docker 
- doc : https://www.docker.com
- how to write a dockerfile : https://www.educative.io/edpresso/how-do-you-write-a-dockerfile | https://www.codementor.io/@aviaryan/writing-your-first-dockerfile-7e0rjhual 
- plus de détail : https://takacsmark.com/dockerfile-tutorial-by-example-dockerfile-best-practices-2018/ 
- best practice : https://engineering.bitnami.com/articles/best-practices-writing-a-dockerfile.html 
- pour aller plus loin : https://www.katacoda.com/courses/container-runtimes 
