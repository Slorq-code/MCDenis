import React, { useEffect } from 'react';
import Card from '../components/card';
import '../styles/components/grid.css';
import '../styles/generic.css';

function Grid() {
  useEffect(() => {
    function handleMouseScroll(event) {
      const deltaY = event.deltaY || event.detail || event.wheelDelta;
      event.preventDefault();
      window.scrollBy({ 
        left: deltaY,
        behavior: 'smooth'
      });
    }
    document.addEventListener('mousewheel', handleMouseScroll, { passive: false });
    document.addEventListener('DOMMouseScroll', handleMouseScroll, { passive: false });
    return () => {
      document.removeEventListener('mousewheel', handleMouseScroll);
      document.removeEventListener('DOMMouseScroll', handleMouseScroll);
    };
  }, []);
  return (
    <div className="grid">
      <div className='gridContainer'>
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
        <Card />
      </div>
    </div>
  );
}

export default Grid;