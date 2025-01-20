curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o generated grammar/MERLAN.g4