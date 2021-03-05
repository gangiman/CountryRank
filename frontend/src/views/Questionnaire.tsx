import React, { ReactElement, useState } from 'react';
import { Box } from '@material-ui/core';
import { Dropdown, Button } from 'semantic-ui-react'
import { useStyles } from './Questionnaire.styles';
import { COUNTRY_URL } from '../config';



const languagesOptions = [
  { key: 'en', text: 'English', value: 'en' },
  { key: 'fr', text: 'French', value: 'fr' },
  { key: 'gr', text: 'German', value: 'gr' },
  { key: 'sp', text: 'Spanish', value: 'sp' },
]

const primaryOptions = [
  {
    key: 'freedom',
    text: 'Freedom',
    value: 'freedom',
  },
  {
    key: 'business',
    text: 'Business',
    value: 'business',
  },
  {
    key: 'happiness',
    text: 'Happiness',
    value: 'happiness',
  },
  {
    key: 'prosperity',
    text: 'Prosperity',
    value: 'prosperity',
  },
]

export function Questionnaire(): ReactElement {
  const classes = useStyles();
  const [selectedLanguages, setSelectedLanguages] = useState([]);
  const [selectedPriority, setSelectedPriority] = useState(null);
  const handleTagChange = (event: React.SyntheticEvent<HTMLElement>, data: any): void => {
    setSelectedPriority(data.value);
  };
  const handleLanguagesChange = (event: React.SyntheticEvent<HTMLElement>, data: any): void => {
    setSelectedLanguages(data.value);
  };
  const onClick = async () => {
    console.log(selectedPriority);
    console.log(selectedLanguages);
    const response = await fetch(COUNTRY_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ languages: selectedLanguages, priority: selectedPriority })
    });
    console.log(response);
  }
  return (
    <Box className={classes.mainBody}>
      <h2>Which languages would you prefer to speak in the targeted country?</h2>
      <Dropdown
        placeholder='Choose languages'
        fluid
        multiple
        selection
        options={languagesOptions}
        onChange={handleLanguagesChange} />
      <h2>Choose one of the tags to be the primary</h2>
      <Dropdown
        placeholder='Select a tag'
        fluid
        selection
        options={primaryOptions}
        onChange={handleTagChange}
      />
      <Box className={classes.button}>
        <Button primary onClick={async () => {await onClick()}} className={classes.button}>Find your country</Button>
      </Box>
    </Box>
  )
};
