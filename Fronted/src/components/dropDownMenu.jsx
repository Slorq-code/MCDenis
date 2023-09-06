import React from 'react';
import '../styles/generic.css'
import '../styles/components/dropDownMenu.css'

import userWhiteSvg from '../assets/icons/userWhite.svg'; // Importar la imagen SVG
import homeWhiteSvg from '../assets/icons/homeWhite.svg'; // Importar la imagen SVG
import numbersWhiteSvg from '../assets/icons/numbersWhite.svg'; // Importar la imagen SVG
import chatWhiteSvg from '../assets/icons/chatWhite.svg'; // Importar la imagen SVG 
import starWhiteSvg from '../assets/icons/starWhite.svg'; // Importar la imagen SVG
import settingsWhiteSvg from '../assets/icons/settingsWhite.svg'; // Importar la imagen SVG



function DropdownMenu() {
  return (
    <div className="dropdown-menu flexColumn">
      <div className='iconContainer flexColumn' >
        <img className='icon' src={userWhiteSvg} alt="user"/>
      </div>
      <div className='iconContainer flexColumn' >
        <img className='icon' src={homeWhiteSvg} alt="home" />
        <img className='icon' src={numbersWhiteSvg} alt="numbers" />
        <img className='icon' src={chatWhiteSvg} alt="chat" />
        <img className='icon' src={starWhiteSvg} alt="star" />
        <img className='icon' src={settingsWhiteSvg} alt="settings" />
      </div>
    </div>
  );
}

export default DropdownMenu;