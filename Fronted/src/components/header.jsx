import React from 'react';
import '../styles/generic.css'
import '../styles/components/header.css'
import tituloImage from '../assets/image/título.png'


function Header() {
  return (
    <header className='header flexColumn' >
      <img className='marginCero title' src={tituloImage} alt='title' />
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