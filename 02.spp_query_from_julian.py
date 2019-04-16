from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


infile = open("data/image_links.txt", "r")
link = infile.readline()
outfile = open("data/mushroom_toxicity.txt", "w")
outfile.write("Name\tEdible\tPoisonous\n")
browser = webdriver.Firefox()

while link != "":
    spl_link = link.strip("\n").split("/")
    genus, species = spl_link[-1].split("_")[0:2]
    species = species.split("-")[0]
    species = species.split(".")[0]
    browser.get("https://www.ncbi.nlm.nih.gov/pubmed/")
    query = browser.find_element_by_id("term")
    if species != "sp":
        name = genus + " " + species
    else:
        name = genus + " sp"
    query.send_keys(name + Keys.RETURN)
    body = browser.find_element_by_xpath("/html/body")
    corpus = body.text
    good = ["edible", "food"]
    bad = ["poison", "toxic"]
    edible = 0
    poisonous = 0
    for i in good:
        print(i)
        edible += corpus.count(i)
    for i in bad:
        poisonous += corpus.count(i)
    outfile.write(F"{name}\t{edible}\t{poisonous}\n")
    link = infile.readline()
outfile.close()
infile.close()
