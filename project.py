{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "ltLy9wOFouMb"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "\n",
        "def fetch_papers(query: str):\n",
        "    \"\"\"\n",
        "    Fetch paper IDs from PubMed using a search query.\n",
        "    \"\"\"\n",
        "    base_url = \"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi\"\n",
        "    params = {\n",
        "        \"db\": \"pubmed\",\n",
        "        \"term\": query,\n",
        "        \"retmode\": \"json\",\n",
        "        \"retmax\": 100  # Fetch up to 100 papers for simplicity\n",
        "    }\n",
        "\n",
        "    response = requests.get(base_url, params=params)\n",
        "    response.raise_for_status()  # Raise an error for bad responses\n",
        "    data = response.json()\n",
        "    return data.get(\"esearchresult\", {}).get(\"idlist\", [])\n"
      ],
      "metadata": {
        "id": "jmxeg5ROowcO"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import xml.etree.ElementTree as ET\n",
        "from xml.etree import ElementTree\n",
        "def fetch_paper_details(id):\n",
        "  filtered_papers = []\n",
        "  non_academic_authors = []\n",
        "  company_affiliations = []\n",
        "  params = {\"db\":\"pubmed\",\"id\":id, \"retmode\":\"xml\"}\n",
        "  base_url = \"http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi\"\n",
        "  response = requests.get(base_url, params)\n",
        "  root = ElementTree.fromstring(response.content)\n",
        "  for article in root.findall(\"PubmedArticle\"):\n",
        "    title = article.find('.//ArticleTitle')\n",
        "    date = article.find('.//ArticleDate')\n",
        "    year = date.find('.//Year')\n",
        "    month = date.find('.//Month')\n",
        "    day = date.find('.//Day')\n",
        "    print(year.text+ month.text+day.text)\n",
        "    authors = article.find(\".//AuthorList\")\n",
        "    if(authors is None):\n",
        "      continue\n",
        "    if(len(authors) == 0):\n",
        "      continue\n",
        "    for author in authors:\n",
        "      lastName = author.find(\".//LastName\").text\n",
        "      foreName = author.find(\".//ForeName\").text\n",
        "      Intial = author.find(\".//Initials\").text\n",
        "      afList = author.find('.//AffiliationInfo')\n",
        "      name = lastName+\"   \"+foreName+\"   \"+Intial\n",
        "      if(afList is None):\n",
        "        continue\n",
        "      if(len(afList) == 0):\n",
        "        continue\n",
        "      for affiliation in afList:\n",
        "        if affiliation is not None and \"Inc\" in affiliation or \"LLC\" in affiliation or \"Corp\" in affiliation:\n",
        "          company_affiliations.append(affiliation.text)\n",
        "      if len(company_affiliations) != 0:\n",
        "        non_academic_authors.append(name)\n",
        "    if non_academic_authors:\n",
        "          filtered_papers.append({\n",
        "                \"PubmedID\": id,\n",
        "                \"Title\": title,\n",
        "                \"Publication Date\": year.text+ month.text+day.text,\n",
        "                \"Non-academic Author(s)\": \", \".join(non_academic_authors),\n",
        "                \"Company Affiliation(s)\": \", \".join(company_affiliations)\n",
        "            })\n",
        "    return filtered_papers\n",
        "\n"
      ],
      "metadata": {
        "id": "JQM7g9ajo1v4"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "ids = [ 39847825 ,  39847811 ,  39847800 ,  39847788 ,  39847771 ,  39847761 ,  39847746 ,  39847745 ,  39847744 ,  39847743 ,  39847736 ,  39847732 ,  39847613 ,  39847598 ,  39847593 ,  39847582 ,  39847581 ,  39847579 ,  39847533 ,  39847517 ,  39847514 ,  39847509 ,  39847504 ,  39847469 ,  39847462 ,  39847453 ,  39847434 ,  39847385 ,  39847372 ,  39847363 ,  39847350 ,  39847346 ,  39847292 ,  39847288 ,  39847284 ,  39847282 ,  39847281 ,  39847267 ,  39847248 ,  39847239 ,  39847238 ,  39847237 ,  39847233 ,  39847232 ,  39847226 ,  39847224 ,  39847205 ,  39847203 ,  39847190 ,  39847188 ,  39847185 ,  39847178 ,  39847175 ,  39847172 ,  39847168 ,  39847163 ,  39847154 ,  39847153 ,  39847145 ,  39847143 ,  39847133 ,  39847131 ,  39847129 ,  39847119 ,  39847116 ,  39847110 ,  39847107 ,  39847099 ,  39847077 ,  39847074 ,  39847055 ,  39846985 ,  39846984 ,  39846983 ,  39846982 ,  39846981 ,  39846970 ,  39846966 ,  39846957 ,  39846954 ,  39846951 ,  39846879 ,  39846810 ,  39846804 ,  39846802 ,  39846761 ,  39846674 ,  39846615 ,  39846613 ,  39846611 ,  39846608 ,  39846549 ,  39846541 ,  39846480 ,  39846465 ,  39846444 ,  39846434 ,  39846431 ,  39846417 ,  39846413 ]\n",
        "for id in ids:\n",
        "  fetch_paper_details(id)\n",
        "\"\"\"\n",
        "id = 39847736\n",
        "ar = fetch_paper_details(id)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VcRjvpk28BLP",
        "outputId": "10cecc85-7962-4364-d539-5a06ec9e77ba"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20250124\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def filter_non_academic_papers(papers):\n",
        "    \"\"\"\n",
        "    Filter papers with at least one author affiliated with a non-academic organization.\n",
        "    \"\"\"\n",
        "    filtered_papers = []\n",
        "    for paper in papers:\n",
        "        non_academic_authors = []\n",
        "        company_affiliations = []\n",
        "\n",
        "        for author in paper[\"Authors\"]:\n",
        "            affiliation = author.get(\"affiliation\", \"\")\n",
        "            # Check for company-like keywords in affiliations\n",
        "            if \"Inc\" in affiliation or \"LLC\" in affiliation or \"Corp\" in affiliation:\n",
        "                non_academic_authors.append(author.get(\"name\", \"\"))\n",
        "                company_affiliations.append(affiliation)\n",
        "\n",
        "        if non_academic_authors:\n",
        "            filtered_papers.append({\n",
        "                \"PubmedID\": paper[\"PubmedID\"],\n",
        "                \"Title\": paper[\"Title\"],\n",
        "                \"Publication Date\": paper[\"Publication Date\"],\n",
        "                \"Non-academic Author(s)\": \", \".join(non_academic_authors),\n",
        "                \"Company Affiliation(s)\": \", \".join(company_affiliations)\n",
        "            })\n",
        "\n",
        "    return filtered_papers\n"
      ],
      "metadata": {
        "id": "44v2--jpo6bh"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "def save_to_csv(papers, filename=\"results.csv\"):\n",
        "    \"\"\"\n",
        "    Save the filtered paper data to a CSV file.\n",
        "    \"\"\"\n",
        "    df = pd.DataFrame(papers)\n",
        "    df.to_csv(filename, index=False)\n",
        "    print(f\"Results saved to {filename}.\")\n"
      ],
      "metadata": {
        "id": "MNzhKKsBo-dU"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def main(query, filename=\"results.csv\"):\n",
        "    print(f\"Fetching papers for query: {query}...\")\n",
        "    pubmed_ids = fetch_papers(query)\n",
        "    print(f\"Fetched {len(pubmed_ids)} paper IDs.\")\n",
        "\n",
        "    if not pubmed_ids:\n",
        "        print(\"No papers found.\")\n",
        "        return\n",
        "\n",
        "    print(\"Fetching paper details...\")\n",
        "    filtered_papers = []\n",
        "    for pubMedid in pubmed_ids:\n",
        "      filtered_papers = fetch_paper_details(pubMedid)\n",
        "      if not filtered_papers:\n",
        "          print(\"No papers found with non-academic authors.\")\n",
        "          return\n",
        "      if filtered_papers:\n",
        "        print(f\"Found {len(filtered_papers)} papers with non-academic authors.\")\n",
        "        save_to_csv(filtered_papers, filename)\n"
      ],
      "metadata": {
        "id": "UyTUubO0pBld"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Example usage\n",
        "query = \"cancer treatment\"\n",
        "filename = \"sample.csv\"\n",
        "\n",
        "main(query, filename)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KNT8GBqXpECL",
        "outputId": "1938176c-3f88-4dc6-c57b-74a98433eb79"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Fetching papers for query: cancer treatment...\n",
            "Fetched 100 paper IDs.\n",
            "Fetching paper details...\n",
            "20250124\n",
            "No papers found with non-academic authors.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "pWq9BzuuquBY"
      },
      "execution_count": 7,
      "outputs": []
    }
  ]
}