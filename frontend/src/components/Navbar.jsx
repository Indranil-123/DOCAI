import React from 'react'
import {assets} from '../assets/assets'
import { NavLink } from 'react-router-dom'

const Navbar = () => {
  return (
    <div>
        <img src={assets.logo} alt="" />
        <ul>
            <NavLink>
                <li>Home</li>
                <hr />
            </NavLink>
            <NavLink>
                <li>Doctors</li>
                <hr />
            </NavLink>
            <NavLink>
                <li>About Us</li>
                <hr />
            </NavLink>
            <NavLink>
                <li>Contact</li>
                <hr />
            </NavLink>
            <NavLink>
                <li>AI Assistance</li>
                <hr />
            </NavLink>
        </ul>
      
    </div>
  )
}

export default Navbar
