# Unit-Convertor
Unit Convertor is a dashboard application that can convert units for the follwoing parameters length, pressure, and temperature.
##Table of contents
1. [Installation](#installation)
2. [Usage](#usage)
4. [License](#license)
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/johnblessmbunga/Unit-Convertor.git
   cd Unit-Convertor
   npm install
## Usage
To strat application ,run:

npm start
### Features
__-Dashboard__: contains a dashboard for user input. Initially the dashboard is set to the homepage
### Figure 1: Homepage
![Homepage](images/Homepage.png)


__-Brackets__: Can use brackets in equations with symbols \(\) other brackets such as \[\] and \{\} are not accepted. When two adjacent bracket elements or a number element follwed by a bracket element the result of the commputation is the product of the two elements.

__-Positive & Negative Handling__: Recognises + or - before a number or bracket element as  an indication of a positive or negative element. Additionaly Arithemtic-Calculator can simplify multiple adjacent + or/and - signs into a single + or - sign.

__-Space & Error Handling__: Is capable of handling whether spaces are included, not included, or a combination of both. Arithemtic-Calculator also produces error message if unclosed bracket, random string, invalid operation detected.
## License
This project is licensed under MIT license.

### Acknowledgements
Thanks to the os library for providing backend framework.
