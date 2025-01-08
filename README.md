The data was extracted form the open source SEC dataset and the task was to extract the dates of violation, company names, SEC employees, Convicts and any dollar amounts. Python's en_core_web_lg module was used to extract the data in all the cases. We checked the data to the entities in en_core_web_lg and cross-checked the data.

1) For extracting the company details, we mployed the usage of 'ORG' label present in en_core_web_lg and thenwe removed all instaces of SEC from the output (Since it will return SEC also as an  organization). 'SEC','THE SEC','SECURITIES AND EXCHANGE COMMISSION', 'THE SECURITIES AND EXCHANGE COMMISION' were the words used to check.

2) To figure out the dates of violation, the approach we used is to collect all the dates present in the dataframe and then to remove all the dates of filing, which will only give back dates of violation. In order to do that, we created a function called 'new_search' which will take as it's parameters each of the reports present in the dataframe, the date to be searched in that particular report and the number of words to be searched before and after the location of the date. This way, if we see the words 'LITIGATION', 'FILED' or 'MODIFIED' or any words associated with 'SEC' very nearby the date, we can omit that date since it is a date of filing.

3) To print the cmnvict names, we used 'PERSON' label of en_core_web_lg.

4) We used the 'MONEY' label present in en_core_web_lg to print all the dollar amounts.

5) To print the SEC Employees, we used a method whoch was a combination of the second and third questions. We used the new_search function again (from the second question) to go through the dataframe and identify  people associated with SEC by checking the people who have anything related to SEC anywhere near them. 'SEC','THE SEC','SECURITIES AND EXCHANGE COMMISSION', 'THE SECURITIES AND EXCHANGE COMMISION' were the words used to check.
