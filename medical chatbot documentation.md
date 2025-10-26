# MEDICAL RAG CHATBOT

## ✅ Prerequisites Checklist (Complete These Before Moving Forward)

- [ ] **Docker Desktop** is installed and running in the background
- [ ] **Code versioning** is properly set up using GitHub (repository pushed and updated)
- [ ] **Dockerfile** is created and configured for the project
- [ ] **Dockerfile** is also created and configured for **Jenkins**


### Code Versioning Kya Hai?

**Code Versioning** ka seedha sa matlab hai aapke code mein kiye gaye har badlav (change) ka record rakhna. Iske liye hum **Git** ⏳ naam ke tool ka istemaal karte hain.

**GitHub** ☁️ woh online platform (website) hai jahaan aap apne Git project (repository) ko store karte hain, taaki:
1.  Aapka code online safe rahe.
2.  Aapki team (ya aap khud) alag-alag computers se uspar kaam kar sakein.

---

### Aapke Checklist Wale Step Ka Matlab

Aapki checklist mein likha hai: "Code versioning is properly set up using GitHub (repository pushed and updated)".

Iska matlab hai ki pipeline shuru karne se pehle, aapko yeh pakka karna hai ki:

1.  Aapke project ka **saara code** (jaise aapki Python files, `requirements.txt`, `Dockerfile`, aur `Jenkinsfile`) aapke local computer par hai.
2.  Aapne `git add .`, `git commit`, aur `git push` commands ka istemaal karke uss **poore code ko GitHub repository par upload kar diya hai**.

**Saral bhasha mein:** Aapka saara naya aur updated code aapke computer se nikal kar GitHub.com par pahunch jaana chahiye.

---

### Yeh Zaroori Kyun Hai?

Yeh isliye zaroori hai kyunki aapka **Jenkins server 🤖 aapke laptop se code nahi lega**.

Jab pipeline chalegi, toh Jenkins ka sabse pehla kaam hoga aapke **GitHub repository se connect karna** aur wahaan se saara code "checkout" (download) karna.

Agar aapka code GitHub par "pushed" ya "updated" nahi hoga, toh Jenkins purana code utha lega (ya use kuch bhi nahi milega) aur aapki pipeline fail ho jaayegi.

## ==> 1. 🚀 Jenkins Setup for Deployment

### 1. Create Jenkins Setup Directory and Dockerfile

- Create a folder named `custom_jenkins`
- Inside `custom_jenkins`, create a `Dockerfile` and add the necessary Jenkins + Docker-in-Docker configuration code

### 2. Build Jenkins Docker Image

Open terminal and navigate to the folder:

```bash
cd custom_jenkins
```

Make sure **Docker Desktop is running in the background**, then build the image:

```bash
docker build -t jenkins-dind .
```

docker build: Yeh Docker ko bolta hai ki ek nayi image banani hai.

-t jenkins-dind: Yeh uss image ko ek naam (jenkins-dind) de raha hai. -t ka matlab hota hai "tag" ya naam dena.

.: Yeh aakhri dot (.) ka matlab hai ki Dockerfile (jisme image banane ke instructions hote hain) isi current folder mein hai.


### 3. Run Jenkins Container

```bash
docker run -d ^
  --name jenkins-dind ^
  --privileged ^
  -p 8080:8080 ^
  -p 50000:50000 ^
  -v /var/run/docker.sock:/var/run/docker.sock ^
  -v jenkins_home:/var/jenkins_home ^
  jenkins-dind
```


Yeh command aapke `jenkins-dind` image se ek naya Jenkins container shuru (run) kar raha hai.

Is container ko "Docker-in-Docker" (dind) ke liye set up kiya gaya hai. Iska matlab hai ki aapka **Jenkins container khud bhi Docker commands chala sakta hai** (jaise CI/CD pipeline ke dauraan Docker images build karna).

---

### Interview Mein Kaise Explain Karein

Aap is command ko line-by-line (ya flag-by-flag) tod kar samjha sakte hain.

"Yeh `docker run` command ek naya Jenkins container launch kar raha hai, aur iske alag-alag flags (options) yeh kaam karte hain:"

* `docker run`: Yeh naya container banane aur start karne ki main command hai.
* `-d`: Iska matlab hai **"detached mode"**. Yeh container ko background mein chalata hai aur terminal ko free kar deta hai.
* `--name jenkins-dind`: Hum container ko ek aasaan sa naam ('jenkins-dind') de rahe hain, taaki baad mein ise `docker stop` ya `docker start` karna aasan ho.
* `--privileged`: Yeh **sabse zaroori flag hai "Docker-in-Docker" (dind) ke liye**. Yeh flag container ko host machine par poore (root-level) permissions deta hai. Jenkins ko yeh permissions chahiye taaki woh apne andar ek alag se Docker daemon (service) chala sake aur naye containers (jaise build agents) bana sake.
* `-p 8080:8080`: Yeh **port mapping** hai. Yeh host machine (aapke laptop) ke port 8080 ko container ke port 8080 se jodta hai. Isse hum apne browser mein `localhost:8080` daal kar Jenkins ke web interface ko access kar sakte hain.
* `-p 50000:50000`: Yeh port bhi Jenkins agents (slaves) ke liye hai. Yeh Jenkins master aur agents ke beech communication ke liye use hota hai.
* `-v /var/run/docker.sock:/var/run/docker.sock`: Yeh host machine ke **Docker socket** ko container ke andar mount (share) kar raha hai. Yeh bhi ek tarika hai jisse container (Jenkins) host ke Docker daemon se baat kar sakta hai aur Docker commands (jaise `docker build`, `docker run`) chala sakta hai.
* `-v jenkins_home:/var/jenkins_home`: Yeh **data persistence (data ko save rakhne)** ke liye bahut zaroori hai.
    * Yeh `jenkins_home` naam ka ek 'named volume' banata hai.
    * Yeh volume container ke `/var/jenkins_home` folder se link ho jaata hai.
    * Jenkins apni saari settings, plugins, aur jobs isi folder mein rakhta hai.
    * Isse, agar hum container ko stop ya delete bhi kar dein, toh bhi hamara saara Jenkins ka data uss volume mein safe rehta hai aur agle container start par wapas mil jaata hai.
* `jenkins-dind`: Yeh us **Docker image ka naam hai** jise hum run karna chahte hain (jo humne pichle `docker build` command se banayi thi).
* `^`: (Yeh `^` symbol Windows Command Prompt mein "line continuation character" hai. Iska matlab hai ki command abhi khatam nahi hui hai, agli line par jaari hai. Linux/Mac mein iski jagah `\` (backslash) use hota hai.)



> ✅ If successful, you’ll get a long alphanumeric container ID

### 4. Check Jenkins Logs and Get Initial Password

```bash
docker ps
docker logs jenkins-dind
```

If the password isn’t visible, run:

```bash
docker exec jenkins-dind cat /var/jenkins_home/secrets/initialAdminPassword
```

### 5. Access Jenkins Dashboard

- Open your browser and go to: [http://localhost:8080](http://localhost:8080)

### 6. Install Python Inside Jenkins Container

Back in the terminal:

```bash
docker exec -u root -it jenkins-dind bash
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
exit
```

### 7. Restart Jenkins Container

```bash
docker restart jenkins-dind
```



### Jenkins Kya Hai?
**Jenkins ek automation server hai**. Isko aap developers ka ek "smart robot" 🤖 samajh sakte hain.
Iska mukhya kaam software banane ke poore process (jise **CI/CD - Continuous Integration/Continuous Deployment** kehte hain) ko automate karna hai. Ye kaam is prakaar hain:
1.  **Code Lena**: Jaise hi koi developer code likhkar Git par daalta hai, Jenkins use automatically utha leta hai.
2.  **Build Karna**: Us code ko compile karke ek software/application banata hai.
3.  **Test Karna**: Software ko automatically test karta hai taaki usmein koi galti (bug) na ho.
4.  **Deploy Karna**: Agar sab aache se test ho jaata hai, to use server par live kar deta hai.
**Fayda**: Isse kaam tezi se hota hai aur insaani galtiyon ki gunjaish kam ho jaati hai.
-----
### Jenkins Container Kya Hai?
**Jenkins Container** ka matlab hai Jenkins ko seedhe aapke computer ya server par install karne ke bajaye, use ek **Docker container ke andar chalana**.
Ek container ek chhota, isolated "box" 📦 jaisa hota hai jismein Jenkins aur usko chalne ke liye zaroori sab cheezein (jaise Java, operating system files) pehle se pack hoti hain.
**Fayda**:
  * **Aasaan Setup**: Aapko alag se Java ya kuch aur install karne ki zaroorat nahi padti.
  * **Saaf-Suthra (Clean)**: Container ko delete karne par Jenkins se judi har cheez hat jaati hai, aapka system ganda nahi hota.
  * **Portable**: Yeh container aapke laptop, company ke server, ya cloud par—kahin bhi bilkul ek jaisa chalega.
-----


#### 6\. Jenkins Container Ke Andar Python Install Karna

Yeh commands Jenkins container ke **andar** chalai jaa rahi hain.

```bash
# 1. Container ke andar ghusna (Enter the container)
docker exec -u root -it jenkins-dind bash
```

  * `docker exec`: Yeh command pehle se chal rahe container ke andar koi doosri command chalane ke liye hoti hai.
  * `-u root`: Command ko **root user** (admin) ki tarah chalao, taaki software install karne ki permission ho.
  * `-it`: Iska matlab hai **interactive mode** mein jao, yaani aapko container ke andar ek command prompt (terminal) mil jayega.
  * `jenkins-dind`: Yeh us container ka naam hai jiske andar aap ja rahe hain.
  * `bash`: Yeh shell (command prompt) shuru kar deta hai.
    **Aasaan bhasha mein**: Yeh command container ka darwaza kholkar aapko uske andar ek terminal de deti hai.

<!-- end list -->

```bash
# 2. Container ke andar chalne waali commands
apt update -y
apt install -y python3
python3 --version
ln -s /usr/bin/python3 /usr/bin/python
python --version
apt install -y python3-pip
exit
```

  * `apt update -y`: Container ke operating system ko batata hai ki kaun-kaun se naye software available hain.
  * `apt install -y python3`: Python 3 ko install karta hai.
  * `python3 --version`: Check karta hai ki Python 3 sahi se install hua ya nahi.
  * `ln -s /usr/bin/python3 /usr/bin/python`: Yeh ek **shortcut (symlink)** banata hai. Iske baad, jab bhi aap `python` type karenge, to asal mein `python3` chalega. Yeh compatibility ke liye zaroori hota hai.
  * `python --version`: Check karta hai ki shortcut kaam kar raha hai ya nahi.
  * `apt install -y python3-pip`: Python ka package manager `pip` install karta hai, jisse aap Python ki libraries (jaise `requests`, `pandas`) install kar sakte hain.
  * `exit`: Container ke andar ke terminal se bahar aa jaata hai.

-----



### 8. Go to Jenkins Dashboard and Sign In Again

## ==> 2. 🔗 Jenkins Integration with GitHub

### 1. Generate a GitHub Personal Access Token

- Go to **GitHub** → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
- Click **Generate new token (classic)**
- Provide:
  - A **name** (e.g., `Jenkins Integration`)
  - Select scopes:
    - `repo` (for full control of private repositories)
    - `admin:repo_hook` (for webhook integration)

- Generate the token and **save it securely** (you won’t see it again!).

> ℹ️ **What is this token?**
> A GitHub token is a secure way to authenticate Jenkins (or any CI/CD tool) to access your GitHub repositories without needing your GitHub password. It's safer and recommended over using plain credentials.

---

### 2. Add GitHub Token to Jenkins Credentials

- Go to **Jenkins Dashboard** → **Manage Jenkins** → **Credentials** → **(Global)** → **Add Credentials**
- Fill in the following:
  - **Username:** Your GitHub username
  - **Password:** Paste the GitHub token you just generated
  - **ID:** `github-token`
  - **Description:** `GitHub Token for Jenkins`

Click **Save**.

---

### 3. Create a New Pipeline Job in Jenkins

- Go back to **Jenkins Dashboard**
- Click **New Item** → Select **Pipeline**
- Enter a name (e.g., `medical-rag-pipeline`)
- Click **OK** → Scroll down, configure minimal settings → Click **Save**

> ⚠️ You will have to configure pipeline details **again** in the next step

---


Jenkins mein "Pipeline" ka matlab hai aapke software ko banane aur release karne ka poora **automated process**.

Isko ek **factory ki assembly line** 🏭 jaisa samjho:

1.  **Code Aata Hai**: Developer code likhta hai (Jaise raw material).
2.  **Stage 1: Build**: Pipeline code ko automatically compile karke ek software banata hai.
3.  **Stage 2: Test**: Pipeline us software ko automatically test karta hai (Quality check).
4.  **Stage 3: Deploy**: Agar sab test pass ho jaate hain, to pipeline use automatically server par daal deta hai (Packing aur shipping).

Toh, "**Create a New Pipeline Job**" ka matlab hai ki aap Jenkins mein ek naya item bana rahe ho jo is poori assembly line (process) ko chalaayega.

Yeh saare steps (`Build`, `Test`, `Deploy`) ek special file mein likhe jaate hain jise **`Jenkinsfile`** kehte hain. Jenkins bas uss file ko padhta hai aur uske hisaab se saara kaam automatically kar deta hai.



### 4. Generate Checkout Script from Jenkins UI

- In the left sidebar of your pipeline project, click **Pipeline Syntax**
- From the dropdown, select **`checkout: General SCM`**
- Fill in:
  - SCM: Git
  - Repository URL: Your GitHub repo URL
  - Credentials: Select the `github-token` you just created
- Click **Generate Pipeline Script**
- Copy the generated Groovy script (e.g., `checkout([$class: 'GitSCM', ...])`)

---


**Seedha Jawab (Short Answer):**

Iska matlab hai ki aap Jenkins ke andar ek **code generator tool** ka istemaal kar rahe hain.

Yeh tool aapko woh specific code (Groovy script) generate karke deta hai jo Jenkins ko aapka project code GitHub se download (ya "checkout") karne ke liye chahiye.

---

### Detail Mein Explanation

Jenkins mein pipeline *code* (ek `Jenkinsfile`) ke zariye chalti hai. Agar aapko pipeline ko yeh bolna hai ki "GitHub jao aur mera project code download karo," toh aapko iske liye Groovy language mein `checkout` command likhni padegi.

Yeh code likhna naye users ke liye mushkil ho sakta hai.

Isliye Jenkins ek helper deta hai jiska naam hai **`Pipeline Syntax`**:

1.  Aap **`Pipeline Syntax`** par click karte hain.
2.  Aap form mein aasaan English mein batate hain ki aapko kya karna hai (Jaise: SCM = `Git`, Repository URL = `aapka_github_link`, Credentials = `aapka_token`).
3.  Jab aap **`Generate Pipeline Script`** par click karte hain, Jenkins uss form ko Groovy code mein badal deta hai.
4.  Aap bas uss generate kiye gaye code ko copy karke apne `Jenkinsfile` mein paste kar dete hain.

**Saral Bhasha Mein:** Yeh ek "translator" 🤖 jaisa hai. Aap ise aasaan bhasha (form) mein batate hain, aur yeh aapko Jenkins ki technical bhasha (Groovy script) mein badal kar de deta hai. Isse galti hone ka chance kam ho jaata hai.



### 5. Create a `Jenkinsfile` in Your Repo ( Already done )

- Open your project in **VS Code**
- Create a file named `Jenkinsfile` in the root directory


### 6. Push the Jenkinsfile to GitHub

```bash
git add Jenkinsfile
git commit -m "Add Jenkinsfile for CI pipeline"
git push origin main
```

---

### 7. Trigger the Pipeline

- Go to **Jenkins Dashboard** → Select your pipeline → Click **Build Now**

🎉 **You’ll see a SUCCESS message if everything works!**

✅ **Your GitHub repository has been cloned inside Jenkins’ workspace!**

---

> 🔁 If you already cloned the repo with a `Jenkinsfile` in it, you can skip creating a new one manually.

## ==> 3. 🐳 Build Docker Image, Scan with Trivy, and Push to AWS ECR

### 1. Install Trivy in Jenkins Container

```bash
docker exec -u root -it jenkins-dind bash
apt install -y
curl -LO https://github.com/aquasecurity/trivy/releases/download/v0.62.1/trivy_0.62.1_Linux-64bit.deb
dpkg -i trivy_0.62.1_Linux-64bit.deb
trivy --version
exit
```

Yeh commands aapke **Jenkins container ke andar 'Trivy' naam ka ek tool install kar rahe hain.**

**Trivy 🛡️ ek open-source security scanner hai.** Iska kaam aapki Docker images ya code ko scan karke yeh batana hai ki unmein koi jaani-maani **vulnerabilities** (security kamzoriyan) ya galat configurations toh nahi hain.

Yeh CI/CD pipeline ka ek bahut zaroori hissa hai.

---

### Interview Mein Kaise Explain Karein

"Yeh script Jenkins container ke andar Trivy security scanner ko set up kar rahi hai, taaki hum pipeline ke dauraan apni Docker images ko scan kar sakein. Iske steps yeh hain:"

1.  `docker exec -u root -it jenkins-dind bash`
    * "Pehle, hum `docker exec` command se `jenkins-dind` container ke andar 'root' user bankar login kar rahe hain, taaki humein software install karne ki permission ho."

2.  `apt install -y`
    * (Yahan aapke command mein ek chhota sa typo/galti hai, ismein package ka naam missing hai. Yeh shayad `apt update -y` ya `apt install -y curl` hona chahiye tha, taaki agla step kaam kar sake. Main maan raha hoon ki `curl` install karna tha ya woh pehle se hai.)

3.  `curl -LO ...trivy_0.62.1_Linux-64bit.deb`
    * "Is `curl` command se hum internet (GitHub releases) se Trivy ka installer package (`.deb` file) download kar rahe hain."
    * `-L` ka matlab hai 'location' (redirects ko follow karo).
    * `-O` ka matlab hai 'output', yaani file ko usi naam se save karo jis naam se woh download ho rahi hai.

4.  `dpkg -i trivy_0.62.1_Linux-64bit.deb`
    * "`dpkg` (Debian package manager) command ka istemaal karke hum us download ki gayi `.deb` file se Trivy ko container ke andar install kar rahe hain."

5.  `trivy --version`
    * "Yeh command hum Tivy ka version check karne ke liye chala rahe hain. Isse yeh pakka ho jaata hai ki installation sahi se ho gaya hai."

6.  `exit`
    * "Aakhir mein, hum `exit` karke container ke terminal se bahar aa jaate hain."

**Saral bhasha mein:** "Hum container ke andar jaakar, Trivy ko internet se download karke install kar rahe hain, taaki Jenkins iska istemaal security scanning ke liye kar sake."

Then restart the container:

```bash
docker restart jenkins-dind
```

---

### 2. Install AWS Plugins in Jenkins

- Go to **Jenkins Dashboard** → **Manage Jenkins** → **Plugins**
- Install:
  - **AWS SDK**
  - **AWS Credentials**
- Restart the Jenkins container:



Yeh instructions bata rahe hain ki Jenkins ko Amazon Web Services (AWS) ke saath jodne (connect) ke liye zaroori "add-ons" ya "tools" install karein.

### AWS Plugins Kya Hain? 🔌

**AWS Plugins** chhote software add-ons hain jo aap Jenkins mein install karte hain. Yeh plugins Jenkins ko **AWS (Amazon Web Services) se baat karne** aur uski alag-alag services (jaise ECR, S3, EC2) ko istemaal karne ki taakat (capability) dete hain.

Bina in plugins ke, Jenkins ko nahi pata ki AWS kya hai ya usse kaise connect karna hai.

---

### In Dono Plugins Ka Kya Kaam Hai?

Aap do khaas plugins install kar rahe hain:

1.  **AWS SDK (Software Development Kit)**
    * Yeh mukhya "toolbox" 🧰 ya "dictionary" hai.
    * Yeh Jenkins ko AWS ki saari services se baat karne ke liye zaroori core commands aur libraries deta hai. Agar aapko AWS ECR (Elastic Container Registry) par image push karni hai, S3 se files download karni hain, ya EC2 par server banana hai, toh yeh plugin zaroori hai.

2.  **AWS Credentials**
    * Yeh ek "safe" ya "digital locker" 🔒 hai.
    * AWS ko access karne ke liye aapko `Access Key` aur `Secret Key` (jo aapke password jaise hote hain) ki zaroorat hoti hai.
    * Yeh plugin un keys ko Jenkins mein **surakshit (securely)** store karne ka ek standard tareeka deta hai. Isse, aapko apni secret keys ko pipeline scripts mein seedha likhne ki zaroorat nahi padti, jo ki ek bahut hi kharaab aur insecure practice hai.

---

### Baaki Steps Ka Matlab

* **Jenkins Dashboard → Manage Jenkins → Plugins:**
    * Yeh woh jagah hai jahaan se aap Jenkins mein koi bhi naya feature (plugin) install, update, ya remove karte hain.

* **Restart the Jenkins container:**
    * `docker restart jenkins-dind`
    * Jab bhi aap koi naya plugin install karte hain, toh woh turant chalu (activate) nahi hota. Jenkins ko **restart karna zaroori hota hai** taaki woh naye install kiye gaye plugins ko load kar sake aur unka istemaal shuru kar sake.



```bash
docker restart jenkins-dind
```

---

### 3. Create IAM User in AWS

- Go to **AWS Console** → **IAM** → **Users** → **Add User**
- Assign **programmatic access**
- Attach policy: `AmazonEC2ContainerRegistryFullAccess`
- After creation, generate **Access Key + Secret**

---


Yeh steps aapke Jenkins (jo ek application hai) ko AWS se securely connect karne ke liye ek special "identity" bana rahe hain.

---

### IAM Kya Hai? (What is IAM?)

**IAM** ka matlab hai **Identity and Access Management**.

Yeh aapke AWS account ka "security guard" 💂 ya "manager" hai. Iska kaam yeh decide karna hai ki:
* **Kaun** (Who): Kaun sa user ya kaun si service (jaise aapka Jenkins).
* **Kya** (What): Kya kar sakta hai (jaise, file read kar sakta hai, ya image upload kar sakta hai).
* **Kispar** (Which): Kis AWS resource par (jaise, ECR ya S3 bucket par).

Aap IAM ka istemaal yeh sunishchit karne ke liye karte hain ki koi bhi vyakti ya application aapke root account (main master account) ka istemaal na kare aur sirf utna hi kaam kar paaye jitni use permission hai.

---

### IAM User Kya Hai? (What is an IAM User?)

Ek **IAM User** ek "identity" hai jo aap apne AWS account ke *andar* banate hain. Yeh aapka main (root) account nahi hai.

Is "user" ko aap kisi insaan ko (jaise ek developer) ya kisi application ko (jaise aapka **Jenkins server**) de sakte hain.

**Aasaan Bhasha Mein:**

* Aapka **Root Account** poori building (AWS account) ki **master key** 🔑 hai. Aap ise kabhi kisi ko nahi dete.
* Ek **IAM User** ek "employee key card" hai. Aap Jenkins ke liye ek special key card bana rahe hain, jise sirf vahi karne ki permission hogi jo aap chahte hain.

---

### In Steps Ka Matlab Kya Hai? (Explanation of Your Steps)

Aap Jenkins ko AWS se jodne ke liye ek "Robot User" (bot user) bana rahe hain:

1.  **Go to AWS Console → IAM → Users → Add User**
    * Iska matlab hai: AWS management website par jao, IAM service kholo, aur ek naya user banane ka process shuru karo.

2.  **Assign programmatic access (Programmatic Access Dena)**
    * Yeh **sabse zaroori** step hai. Iska matlab hai ki yeh user ek **insaan** nahi hai jo website par login karega.
    * Yeh ek **application** (robot/script) hai, jaise ki aapka Jenkins.
    * Ise select karne par hi AWS aapko woh cheez dega jo Jenkins ko chahiye: **Access Key** aur **Secret Key**.

3.  **Attach policy: `AmazonEC2ContainerRegistryFullAccess`**
    * **Policy** ka matlab hai "permission ki list" 📜.
    * Yeh policy (`AmazonEC2ContainerRegistryFullAccess`) uss naye user ko yeh shakti deti hai ki woh aapke **ECR (Elastic Container Registry)** par poora control rakh sake.
    * Aap yeh permission isliye de rahe hain kyunki aapke Jenkins pipeline ka kaam Docker image ko build karke ECR mein **push (upload)** karna hai. Is permission ke bina, AWS aapke Jenkins ki request ko reject (block) kar dega.

4.  **After creation, generate Access Key + Secret**
    * Jab user ban jaata hai, AWS aapko do unique "passwords" dega:
        1.  **Access Key ID** (Yeh username jaisa hota hai, public hota hai)
        2.  **Secret Access Key** (Yeh password jaisa hota hai, ise chhupa kar rakhna hota hai)
    * Aap in dono keys ko copy karke Jenkins ke andar `AWS Credentials` plugin (jo aapne pehle install kiya tha) mein securely save kar denge. Is tarah aapka Jenkins in keys ka istemaal karke AWS mein login kar paayega.



### 4. Add AWS Credentials to Jenkins

- Go to **Jenkins Dashboard** → **Manage Jenkins** → **Credentials**
- Click on **(Global)** → **Add Credentials**
- Select **AWS Credentials**
- Add:
  - **Access Key ID**
  - **Secret Access Key**
- Give an ID (e.g., `aws-ecr-creds`) and Save

---


Yeh steps aapke Jenkins ko batate hain ki aapke AWS account ka "username aur password" kya hai, taaki Jenkins aapke behalf par AWS mein login kar sake.

Aapne pichle step mein AWS mein jo **Access Key** aur **Secret Key** banayi thi, woh aap yahaan Jenkins ke andar ek "safe locker" mein daal rahe hain.

---

### In Steps Ka Matlab Kya Hai?

1.  **Go to Jenkins Dashboard → Manage Jenkins → Credentials**
    * Iska matlab hai aap Jenkins ki main settings mein jaakar uske "Credentials Manager" (jahaan saare password save hote hain) ko khol rahe hain.

2.  **Click on (Global) → Add Credentials**
    * `Global` ka matlab hai ki yeh password Jenkins ke *kisi bhi* project (pipeline) mein istemaal ho sakta hai.
    * Aap "Naya Password/Credential jodo" par click kar rahe hain.

3.  **Select `AWS Credentials`**
    * Yahaan aap Jenkins ko bata rahe hain ki aap jo password save kar rahe hain woh "Amazon Web Services" (AWS) ka hai.
    * Yeh option aapko isliye dikh raha hai kyunki aapne pehle **`AWS Credentials` plugin** install kiya tha.

4.  **Add: Access Key ID / Secret Access Key**
    * Yeh do form fields hain. Yahaan aap AWS se copy ki gayi **Access Key** aur **Secret Key** ko paste karte hain. Jenkins inhein encrypt karke securely store kar leta hai.

5.  **Give an ID (e.g., `aws-ecr-creds`) and Save**
    * Yeh **bahut zaroori** hai. Aap in credentials ko ek "nickname" (jaise `aws-ecr-creds`) de rahe hain.
    * **Fayda**: Jab aap pipeline script (`Jenkinsfile`) likhenge, tab aapko asli Secret Key wahaan nahi likhni padegi. Aap bas yeh **ID (`aws-ecr-creds`)** likhenge. Jenkins khud samajh jaayega ki is ID ka matlab woh saved Access Key aur Secret Key hai.
    * Isse aapki Secret Key hamesha chhipi hui aur surakshit rehti hai.




### 5. Install AWS CLI Inside Jenkins Container

```bash
docker exec -u root -it jenkins-dind bash
apt update
apt install -y unzip curl
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
aws --version
exit
```


**AWS CLI** ka matlab hai **AWS Command Line Interface** ⌨️.

Yeh ek tool hai jo aapko apne computer ke **terminal (command line)** se hi poore AWS account ko control karne ki power deta hai.

Aapko har kaam ke liye AWS ki website (Console) par jaakar button click karne ki zaroorat nahi padti. Aap seedha commands type kar sakte hain, jaise:
* `aws s3 cp ...` (files ko S3 par copy karne ke liye)
* `aws ecr push ...` (Docker image ko ECR par upload karne ke liye)
* `aws ec2 start-instances ...` (Server chalu karne ke liye)

### Jenkins Ko Iski Zaroorat Kyun Hai?

Jenkins ek automation server hai 🤖; woh insaanon ki tarah website par "click" nahi kar sakta.

Jenkins ko AWS se baat karne ke liye commands ki zaroorat hoti hai. AWS CLI, Jenkins ko yeh commands provide karta hai. Jab aapki pipeline chalegi, toh Jenkins parde ke peeche (background mein) `aws ...` commands hi chalaayega.

Jab Jenkins is CLI ka istemaal karta hai, toh yeh automatically woh **Access Key** aur **Secret Key** (jo aapne `aws-ecr-creds` ID se save kiye the) istemaal karke AWS mein login kar lega.

---

### In Commands Ka Matlab Kya Hai?

Yeh script aapke Jenkins container ke andar AWS CLI tool ko install kar rahi hai.

1.  `docker exec -u root -it jenkins-dind bash`
    * "Hum `docker exec` se `jenkins-dind` container ke andar 'root' user (admin) bankar login kar rahe hain."

2.  `apt update`
    * "Container ke software package list ko update kar rahe hain."

3.  `apt install -y unzip curl`
    * "Hum do zaroori helper tools install kar rahe hain:
        * `curl`: Internet se files download karne ke liye.
        * `unzip`: `.zip` files ko extract (kholne) ke liye."

4.  `curl "https://..." -o "awscliv2.zip"`
    * "Hum `curl` ka istemaal karke AWS CLI (Version 2) ka official installer, jo ek `.zip` file hai, download kar rahe hain aur use `awscliv2.zip` naam se save kar rahe hain."

5.  `unzip awscliv2.zip`
    * "Us download ki gayi zip file ko `unzip` kar rahe hain. Isse ek `aws` naam ka naya folder ban jaayega."

6.  `./aws/install`
    * "Us `aws` folder ke andar ek `install` script hai. Hum us script ko chala rahe hain. Yeh script AWS CLI tool ko container ke system mein sahi se install kar deti hai."

7.  `aws --version`
    * "Hum `aws --version` chala kar check kar rahe hain ki AWS CLI sahi se install hua ya nahi."

8.  `exit`
    * "Install hone ke baad, hum container ke terminal se `exit` (bahar) aa jaate hain."



---

### 6. Create an ECR Repository

- Go to AWS Console → ECR → Create Repository
- Note the **repository URI**

---

### AWS ECR Kya Hai?

**ECR** ka matlab hai **Elastic Container Registry**.

Yeh AWS ki taraf se di gayi ek **private Docker image "godown" (warehouse)** 📦 hai.

* **Docker Hub** (jahaan se aap `ubuntu` ya `python` jaisi images lete hain) ek *public* registry hai, jaise ek public library.
* **ECR** aapka apna *private* registry hai, jaise aapka apna personal "locker" ya "godown".

Aap apni company ki applications ki jo Docker images banate hain, unhe aap public mein nahi rakhna chahte. Aap unhe ECR mein **securely store** karte hain.

Aapki CI/CD pipeline ka main kaam yahi hai:
1.  Code se Docker image banana.
2.  Us image ko is private ECR godown mein **push (upload)** karna.

---

### Is Step Ka Matlab Kya Hai? (Explanation of Step 6)

`Go to AWS Console → ECR → Create Repository`
* Iska matlab hai ki aap us bade se "godown" (ECR) ke andar apne naye project (jaise `my-python-app`) ke liye ek **khaas "shelf" ya "section"** bana rahe hain.
* Is "repository" ka aap ek naam denge. Aapke project ke saare versions (jaise `v1.0`, `v1.1`, `latest`) isi ek repository ke andar store honge.

`Note the repository URI`
* Jab aap yeh repository banate hain, AWS aapko ek **unique address** deta hai. Ise **Repository URI** (Uniform Resource Identifier) kehte hain.
* Yeh URI kuch aisa dikhta hai:
    `123456789012.dkr.ecr.us-east-1.amazonaws.com/my-python-app`
* Yeh **bahut zaroori hai** kyunki yeh aapke uss naye "shelf" ka poora pata (address) hai.
* Aapko is URI ko copy karke rakhna hai. Jab aap Jenkins pipeline (`Jenkinsfile`) banayenge, tab aapko Jenkins ko yahi URI batana hoga ki "Docker image ko build karne ke baad **is pate par** bhej do (push kar do)."


### 7. Add Build, Scan, and Push Stage in Jenkinsfile (  Already done if cloned )


> 🔐 **Tip**: Change `--exit-code 0` to `--exit-code 1` in Trivy to make the pipeline fail on vulnerabilities.

---

Yeh step aapke `Jenkinsfile` (pipeline script) ke uss hisse ke baare mein hai jahaan asali kaam hota hai.

---

### "Build, Scan, and Push" Stage Kya Hai?

Yeh aapki CI/CD pipeline ka sabse zaroori "stage" (hissa) hai. Is stage mein Jenkins teen kaam ek ke baad ek karta hai:

1.  **Build (Banana) 🏗️:**
    * Yeh aapke code (jo GitHub se aaya hai) aur `Dockerfile` ko leta hai.
    * `docker build` command ka istemaal karke, yeh uss code ko ek **Docker image** mein "pack" karta hai.

2.  **Scan (Check Karna) 🛡️:**
    * Image banne ke baad, lekin ECR par bhejme se *pehle*, Jenkins `Trivy` tool ko chalaata hai.
    * Trivy uss nayi image ko poori tarah scan karke usmein **security problems (vulnerabilities)** dhoondhta hai.

3.  **Push (Bhejna) 🚀:**
    * Agar scan mein koi badi problem nahi milti (ya jaisa bhi aapne set kiya ho), toh pipeline ka aakhri kaam hota hai uss image ko **AWS ECR** (aapke private godown) mein `docker push` command se upload karna.

---

### 🔐 Tip Ka Matlab Kya Hai? (Trivy Exit Code)

Yeh tip **bahut zaroori hai** aur yeh security se juda hai.

Har command jab chalti hai, toh woh ek "exit code" deti hai, jo batata hai ki command safal hui ya nahi:
* **`Exit Code 0`** = "Sab theek hai, main safal raha" (Success 👍)
* **`Exit Code 1`** (ya koi aur non-zero number) = "Kuch gadbad hai, main fail ho gaya" (Failure 👎)

**Ab, Trivy ke do modes hain:**

#### 1. `trivy ... --exit-code 0` (Default/Learning Mode)
* **Matlab:** "Trivy, scan karo. Agar security problems milti hain, toh mujhe bas **report de do**, lekin pipeline ko **fail mat karo**. Aakhir mein `Exit Code 0` (Success) hi bhejna."
* **Kab Use Karein:** Jab aap pipeline naya-naya set kar rahe hain aur sirf *dekhna* chahte hain ki kitni problems hain, lekin build ko rokna nahi chahte.

#### 2. `trivy ... --exit-code 1` (Strict/Production Mode)
* **Matlab:** "Trivy, scan karo. Agar **koi bhi** security problem milti hai, toh pipeline ko **turant fail kar do** aur `Exit Code 1` (Failure) bhejo."
* **Kab Use Karein:** Yeh **asli (production) setup** hai.
* **Fayda:** Yeh pipeline ko insecure (kharab) image ko ECR par push karne se **rok deta hai**. Pipeline wahin fail ho jaayegi, aur developer ko pehle security problems fix karni padengi, tabhi code aage badhega.


### 8. Fix Docker Daemon Issues (If Any)

If you encounter Docker socket permission issues, fix with:

```bash
docker exec -u root -it jenkins-dind bash
chown root:docker /var/run/docker.sock
chmod 660 /var/run/docker.sock
getent group docker
# If group 'docker' exists, skip next line
usermod -aG docker jenkins
exit

docker restart jenkins-dind
```
Then open **Jenkins Dashboard** again to continue.

Yeh commands **permission problems** ko theek kar rahe hain.

**Saral Bhasha Mein:**

Aapne `docker.sock` file ko container ke andar share kiya tha. Yeh file host (aapke computer) ke Docker se baat karne ka ek "special phone" 📞 hai.

**Problem:** Aapke Jenkins container ke andar jo `jenkins` user hai, use uss "special phone" (`docker.sock`) ko istemaal karne ki **permission nahi hai**. Isliye jab Jenkins, Docker command (jaise `docker build`) chalane ki koshish karta hai, toh use "Permission Denied" error milta hai.

**Solution:** Yeh commands `jenkins` user ko uss "phone" ko istemaal karne ki permission dete hain.

---

### Commands Ka Matlab

1.  `docker exec -u root -it jenkins-dind bash`
    * "Main `jenkins-dind` container ke andar 'root' user (admin) bankar jaa raha hoon."

2.  `chown root:docker /var/run/docker.sock`
    * "Main `docker.sock` file ka group 'docker' set kar raha hoon. Iska matlab hai ki jo bhi 'docker' group ka member hai, woh ise access kar sakta hai."

3.  `chmod 660 /var/run/docker.sock`
    * "Main file permissions set kar raha hoon.
        * `6` (Owner `root`): Padh (Read) aur likh (Write) sakta hai.
        * `6` (Group `docker`): Padh (Read) aur likh (Write) sakta hai.
        * `0` (Baaki sab): Kuch nahi kar sakte."

4.  `getent group docker`
    * "Yeh bas check kar raha hai ki container ke andar 'docker' naam ka group pehle se bana hua hai ya nahi."

5.  `usermod -aG docker jenkins`
    * "Yeh **sabse zaroori** command hai. Yeh `jenkins` user ko `docker` group ka **member bana rahi hai**."
    * `-a` (append) - group mein jodo.
    * `-G` (group) - 'docker' group mein.
    * **Fayda:** Kyunki `jenkins` user ab `docker` group ka hissa hai, aur `docker` group ko `docker.sock` file istemaal karne ki permission hai (step 3 se), isliye ab `jenkins` user bhi uss "special phone" ka istemaal kar sakta hai.

6.  `exit`
    * "Main container ke terminal se bahar aa raha hoon."

7.  `docker restart jenkins-dind`
    * "Main container ko **restart** kar raha hoon. Yeh zaroori hai taaki `jenkins` user ki nayi group membership (jo humne step 5 mein di) aache se **apply (laagoo) ho jaaye**."




## ==> 4. 🚀 Deployment to AWS App Runner

### ✅ Prerequisites

1. **Jenkinsfile Deployment Stage** ( Already done if cloned )

### 🔐 IAM User Permissions

- Go to **AWS Console** → **IAM** → Select your Jenkins user
- Attach the policy: `AWSAppRunnerFullAccess`

---
Yeh steps aapki application ko **AWS App Runner** par deploy karne (yaani internet par live karne) ki taiyaari ke baare mein hain.

### AWS App Runner Kya Hai? 🚀

**AWS App Runner** Amazon ki ek service hai jo aapki web application ya API ko chalana (run karna) **bahut aasaan** bana deti hai.

* Aapko server (EC2) set up karne, load balancer lagane, ya complex cluster (jaise EKS/ECS) manage karne ki zaroorat nahi padti.
* Aap bas App Runner ko batate hain ki aapki Docker image **ECR mein kahaan rakhi hai** (jo aapne pichle steps mein push ki thi).
* App Runner us image ko leta hai, use run karta hai, scale karta hai (traffic ke hisaab se) aur aapko ek public URL (link) de deta hai.

---

### In Steps Ka Matlab Kya Hai?

Yeh steps deployment se pehle ki **aakhri permission setting** hai.

#### 1. Jenkinsfile Deployment Stage (Already done...)

* Iska seedha sa matlab hai ki aapke `Jenkinsfile` ke andar `deploy` naam ka stage (hissa) pehle se likha hua hai.
* Us code mein yeh instructions hain ki AWS App Runner service ko kaise create ya update karna hai (aapki ECR image ka istemaal karke).

#### 2. IAM User Permissions (Aapko Yeh Karna Hai)

* **Go to AWS Console → IAM → Select your Jenkins user:**
    * Aap AWS website par jaakar uss `IAM User` ko dhoondh rahe hain jo aapne Jenkins ke liye banaya tha.
* **Attach the policy: `AWSAppRunnerFullAccess`:**
    * Yeh **sabse zaroori** hai. Abhi tak, aapke Jenkins user ke paas sirf ECR (images store karne) ki permission thi.
    * Ab aap use ek **nayi permission** (`AWSAppRunnerFullAccess`) de rahe hain.
    * Yeh permission Jenkins ko shakti (power) deti hai ki woh App Runner service ko **bana (create) sake, update kar sake, aur manage kar sake.**

**Saral Bhasha Mein:** Jaise aapne pehle Jenkins ko "godown (ECR) mein samaan rakhne" ki permission di thi, ab aap use "uss samaan ko display (App Runner) par lagane" ki permission de rahe hain.


### 🌐 Setup AWS App Runner (Manual Step)

1. Go to **AWS Console** → **App Runner**
2. Click **Create service**
3. Choose:
   - **Source**: Container registry (ECR)
   - Select your image from ECR
4. Configure runtime, CPU/memory, and environment variables
5. Set auto-deploy from ECR if desired
6. Deploy the service


Yeh steps aapki Docker image ko AWS ECR se lekar use internet par **live publish** karne ka manual process hain.

Aap AWS ko bata rahe hain ki "Meri yeh image ECR mein rakhi hai, ise lo aur iske liye ek web application bana do."

---

### In Steps Ka Matlab

1.  **Go to AWS Console → App Runner → Create service**
    * Iska matlab hai ki aap AWS website par jaakar "App Runner" service ko khol rahe hain aur ek nayi web service banane ka process shuru kar rahe hain.

2.  **Choose: Source: Container registry (ECR)**
    * Yeh App Runner ko bata raha hai ki aapka application code (source) GitHub par nahi hai, balki ek **pehle se bani hui Docker image** hai jo **ECR** (aapke private godown) mein rakhi hai.

3.  **Select your image from ECR**
    * Yahaan aap ECR ke andar jaakar uss specific image repository ko chunte (select) hain jise Jenkins ne build aur push kiya tha (jaise `my-python-app`).

4.  **Configure runtime, CPU/memory, and environment variables**
    * Yeh service ki "settings" hain:
        * **CPU/Memory**: Aap App Runner ko batate hain ki aapki application ko chalne ke liye kitni power (CPU) aur kitni working space (Memory) ki zaroorat hai.
        * **Environment Variables**: Agar aapki app ko chalne ke liye koi secret keys, database password, ya special settings chahiye, toh woh aap yahaan "environment variables" ke roop mein add karte hain.

5.  **Set auto-deploy from ECR if desired**
    * Yeh ek **automation feature** hai.
    * Agar aap ise on karte hain, toh App Runner ECR par nazar rakhega. Jaise hi Jenkins aapki image ka naya version (jaise `v1.2`) ECR mein push karega, App Runner **apne aap** live application ko uss naye version se update kar dega. Yeh CI/CD ke "CD" (Continuous Deployment) part ko automate kar deta hai.

6.  **Deploy the service**
    * Yeh "Go" button hai. Isko click karne ke baad, App Runner aapki image ko ECR se kheenchta (pull) hai, use server par run karta hai, aur aapko ek **public URL** (link) deta hai. Is URL ko koi bhi internet par khol kar aapki application ko access kar sakta hai.


📺 Follow the tutorial video instructions for correct setup

---

### 🧪 Run Jenkins Pipeline

- Go to **Jenkins Dashboard** → Select your pipeline job
- Click **Build Now**

If all stages succeed (Checkout → Build → Trivy Scan → Push to ECR → Deploy to App Runner):

🎉 **CI/CD Deployment to AWS App Runner is complete!**

✅ Your app is now live and running on AWS 🚀



Yeh aapke poore CI/CD process ka **aakhri step** hai. Iska matlab hai ki ab aap automation ko "Go" button daba rahe hain.

---

### 🧪 Run Jenkins Pipeline (Pipeline Ko Chalana)

* `Go to Jenkins Dashboard → Select your pipeline job`:
    Iska matlab hai ki aap Jenkins ke web interface par jaakar uss pipeline job par click karein jo aapne banayi thi.

* `Click Build Now`:
    Yeh "Start" button hai. Ispe click karte hi Jenkins aapke `Jenkinsfile` mein likhe saare instructions (stages) ko **ek ke baad ek, automatically** chalana shuru kar deta hai.

---

### 🎉 Safal Hone Ka Matlab (Successful Run)

Agar aapki pipeline bina kisi error ke poori chal jaati hai, toh Jenkins yeh saare kaam karega:

1.  **Checkout**: GitHub se aapka naya code download karega.
2.  **Build**: Us code se nayi Docker image banayega.
3.  **Trivy Scan**: Uss image ko security ke liye scan karega.
4.  **Push to ECR**: Agar scan theek raha, toh image ko AWS ECR (private godown) mein upload karega.
5.  **Deploy to App Runner**: AWS App Runner ko batayega ki "nyi image aa gayi hai, application ko isse update kar do."

---

### ✅ Aakhri Result (Final Outcome)

Agar yeh sabhi steps green (pass) ho jaate hain:

**CI/CD Deployment to AWS App Runner poora ho gaya hai!**

Iska matlab hai ki aapki application (app) ab **internet par live hai** 🚀 aur AWS App Runner use chala raha hai. Aap App Runner se mile public URL ko browser mein khol kar apni live app dekh sakte hain.
