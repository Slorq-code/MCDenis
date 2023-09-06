import React from 'react';
import '../styles/generic.css'
import '../styles/components/header.css'


function Header() {
  return (
    <header className='header flexColumn' >
      <h1 className='marginCero' >MCD PANEL</h1>
      <div className='Container flexRow' >
        <nav className='Container' >
        <ul class="containerMenu marginCero">
             <li className="headerOption">
                  <a>Who i am?</a>
             </li>
            <li className="headerOption">
                <a>Work done</a>
            </li>
            <li className="headerOption">
                <a>Contac</a>
            </li>
            <li className="headerOption">
                <a>More</a>
            </li>
        </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;