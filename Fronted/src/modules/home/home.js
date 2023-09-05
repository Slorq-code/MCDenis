import React from 'react';
import Header from '../../components/header';
import DropdownMenu from '../../components/dropDownMenu';
import Grid from '../../components/grid';
import '../../styles/modules/home.css'
import '../../styles/generic.css'

function Home() {
  return (
    <div className="dashBoard flexColumn" >
      <DropdownMenu />
      <Header />
      <Grid />
    </div>
  );
}

export default Home;