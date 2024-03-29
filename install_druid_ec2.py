1) sudo apt update -y
2) sudo apt install openjdk-8-jdk -y
3) wget https://dlcdn.apache.org/druid/28.0.1/apache-druid-28.0.1-bin.tar.gz
4) tar -xzf apache-druid-28.0.1-bin.tar.gz
5) cd apache-druid-28.0.1
6) export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
7) export DRUID_HOME=/home/ubuntu/apache-druid-28.0.1
8) PATH=$JAVA_HOME/bin:$DRUID_HOME/bin:$PATH

./bin/start-micro-quickstart
