import React from 'react';
import '../styles/generic.css'
import '../styles/components/header.css'


function Header() {
  return (
    <header className='header flexColumn' >
      <h1>MCD PANEL</h1>
      <div className='flexRow' >
        <nav>
        <ul class="menu flexRow">
             <li>
                  <a>Who i am?</a>
             </li>
            <li>
                <a>Work done</a>
            </li>
            <li>
                <a>Contac</a>
            </li>
            <li>
                <a>More</a>
            </li>
        </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;