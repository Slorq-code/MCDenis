import React from "react";
import "../styles/components/card.css";
import "../styles/generic.css";
import user from "../assets/icons/userWhite.svg";
import locationExample from '../assets/image/LocationExample.png'

function Card() {
  return (
    <div className="card cardAnimation">
      <img className="cardUser" src={user} alt="agente" />
      <div className="container containerInformation" >
        <span className="cardInformation" >
          Ricardo Jorge
          <br />
          Agudelo Ortiz
        </span>
        <span className="cardInformation" >correo@mcd.com</span>
        <span className="cardInformation" >Ultima conexion: <br/> HOY 04:30PM</span>
        <div className="cardConetion" ></div>
      </div>
      <div className="container" >
        <img className="cardMap" src={locationExample} alt="Ubicacion" />
      </div>
    </div>
  );
}

export default Card;
