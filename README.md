# Quality control list for digital books

Collective work of the Normes & standards working group of the SNE digital commission.

The quality control lists for digital books aim to :

* ensure access to digital books for as many readers as possible, without discrimination as to age, skills, physical or mental abilities, culture, equipment or access methods;
* to build a common quality standard for digital books
* make it easier for professionals to take ownership and give meaning to the actions undertaken;

This work is based on the Opquast Checklist - web quality assurance, 240 rules to improve your sites and take better account of your users - Version 4 - 2020-2025

## Licence
The rules are published under a Creative Commons BY-SA licence. You may use them freely, provided you maintain authorship of the content, via a link to :

* https://www.opquast.com. Opquast is a French registered trademark.
* https://github.com/edrlab/qualebook
* https://creativecommons.org/licenses/by-sa/4.0/

## Rules are available as JSON and CSV Data sets

JSON and CSV outputs are used to export rule data in structured formats that can be consumed by other systems or used for data analysis.

### CSV Export

#### Structure

The CSV export contains all quality rules with 16 columns (semicolon-separated):

| Column | Description | Type |
|--------|-------------|------|
| `title` | Rule title | String |
| `abstract` | Brief description of the rule | String |
| `categories` | Rule categories (semicolon-delimited list) | Array |
| `agrege` | Aggregation identifier | String |
| `description` | Detailed rule description | String |
| `actif` | Active status (1 = active, 0 = inactive) | Boolean |
| `tags` | Labels/tags (semicolon-delimited list, e.g., "Legality", "Accessibility") | Array |
| `objectif` | Objectives/goals (semicolon-delimited list) | Array |
| `Meo` | Best Implementation Practice guidance (semicolon-delimited list) | Array |
| `Controle` | Validation/control criteria (semicolon-delimited list) | Array |
| `Source` | Reference sources (semicolon-delimited list) | Array |
| `Referentiel` | Standards and specifications (semicolon-delimited list, e.g., EPUB, WCAG) | Array |
| `epubcheck` | EPUB validation status | Boolean |
| `ace` | Accessibility checker status | Boolean |
| `humancheck` | Human review status | Boolean |
| `steps` | Process steps (semicolon-delimited list) | Array |

#### URLs

* French: https://edrlab.github.io/qualebook/fr/rules/index.csv
* English: https://edrlab.github.io/qualebook/en/rules/index.csv

#### How to Use

1. **Download the CSV file**: Access the URL above for your desired language.

2. **Import into spreadsheet software**: Open in Excel, Google Sheets, or LibreOffice Calc using semicolon as the delimiter.

3. **Parse array fields**: Fields marked as "Array" contain multiple values separated by semicolons. Split by `;` when processing programmatically.

4. **Use cases**:
   - Rule filtering by category, tags, or status
   - Compliance reporting
   - Integration with QA systems
   - Data analysis and reporting

### JSON Export

#### Structure

The JSON export follows the JSON Feed v1.1 standard and contains all 16 rule fields per item:

**Root object fields:**
- `version`: JSON Feed version
- `title`: Feed title
- `description`: Feed description
- `home_page_url`: Homepage URL
- `feed_url`: JSON feed URL
- `items`: Array of rule objects

**Each rule item contains:**
- `title`, `abstract`, `description`, `agrege`: Text fields
- `categories`, `tags`, `steps`, `objectif`, `Meo`, `Controle`, `Source`, `Referentiel`: Array fields
- `actif`, `epubcheck`, `ace`, `humancheck`: Boolean fields
- `date_published`, `date_modified`: ISO 8601 timestamps
- `id`, `url`: Unique identifier and link to rule

#### URLs

* French: https://edrlab.github.io/qualebook/fr/rules/index.json
* English: https://edrlab.github.io/qualebook/en/rules/index.json

#### Sample Output

```json
{
  "version": "https://jsonfeed.org/version/1.1",
  "title": "Qualebook Rules Database",
  "description": "Quality checklist for digital books - Rule database",
  "home_page_url": "https://edrlab.github.io/qualebook",
  "feed_url": "https://edrlab.github.io/qualebook/en/rules/index.json",
  "items": [
    {
      "title": "Copyright and reuse information is available",
      "date_published": "2024-01-15T10:30:00Z",
      "date_modified": "2025-03-10T14:20:00Z",
      "id": "https://edrlab.github.io/qualebook/en/rules/001/",
      "url": "https://edrlab.github.io/qualebook/en/rules/001/",
      "abstract": "Users must be informed of the rights governing the reuse of content",
      "categories": ["rights management"],
      "agrege": "O4094-E010",
      "description": "Rule #01",
      "actif": 1,
      "tags": ["Legality", "Discoverability"],
      "objectif": ["Inform users about conditions of content publication"],
      "Meo": ["Add metadata to mark copyright information"],
      "Controle": ["Verify presence of copyright notice"],
      "Source": ["Opquast"],
      "Referentiel": ["EPUB 3", "Dublin Core"],
      "epubcheck": false,
      "ace": false,
      "humancheck": true,
      "steps": ["Editorial planning", "Digital production"]
    }
  ]
}
```

#### How to Use

1. **Fetch the JSON**: Download or stream the JSON feed URL.

2. **Parse programmatically**: Use a JSON parser to access rule data.

3. **JavaScript example** (fetch and filter by tag):
   ```javascript
   fetch('https://edrlab.github.io/qualebook/en/rules/index.json')
     .then(response => response.json())
     .then(data => {
       const a11yRules = data.items.filter(rule => 
         rule.tags.includes('Accessibility')
       );
       console.log(`Found ${a11yRules.length} accessibility rules`);
       a11yRules.forEach(rule => {
         console.log(`${rule.title}: ${rule.abstract}`);
       });
     });
   ```

4. **Python example** (search and analyze):
   ```python
   import requests
   
   response = requests.get('https://edrlab.github.io/qualebook/en/rules/index.json')
   data = response.json()
   
   # Find all active rules with humancheck status
   reviewed_rules = [
       rule for rule in data['items']
       if rule['actif'] == 1 and rule['humancheck']
   ]
   
   # Group by category
   by_category = {}
   for rule in reviewed_rules:
       for cat in rule['categories']:
           if cat not in by_category:
               by_category[cat] = []
           by_category[cat].append(rule['title'])
   
   for category, rules in by_category.items():
       print(f"{category}: {len(rules)} rules")
   ```

5. **Use cases**:
   - Build custom rule viewers/dashboards
   - Integrate rules into publishing workflows
   - Create rule recommendation systems
   - Perform automated compliance checks
   - Feed data into other applications

## Deepwiki

This repo documentation is available as [deepwiki](https://deepwiki.com/edrlab/qualebook/)

---

# Built with Hugoplate

<p align="center">Hugoplate is a free starter template built with Hugo, and TailwindCSS, providing everything you need to jumpstart your Hugo project and save valuable time.</p>

<p align="center">Made with ♥ by <a href="https://zeon.studio/"> Zeon Studio</a></p>

## ⚙️ Prerequisites

To start using this template, you need to have some prerequisites installed on your machine.

- [Hugo Extended v0.115+](https://gohugo.io/installation/)
- [Node v18+](https://nodejs.org/en/download/)
- [Go v1.20+](https://go.dev/doc/install)

## 👉 Project Setup

We build this custom script to make your project setup easier. It will create a new Hugo theme folder, and clone the Hugoplate theme into it. Then move the exampleSite folder into the root directory. So that you can start your Hugo server without going into the exampleSite folder. Use the following command to setup your project.

```bash
npm run project-setup
```

## 👉 Install Dependencies

Install all the dependencies using the following command.

```bash
npm install
```

## 👉 Development Command

Start the development server using the following command.

```bash
npm run dev
```
## 📝 License

Copyright (c) 2023 - Present, Designed & Developed by [Zeon Studio](https://zeon.studio/)

**Code License:** Released under the [MIT](https://github.com/zeon-studio/hugoplate/blob/main/LICENSE) license.


