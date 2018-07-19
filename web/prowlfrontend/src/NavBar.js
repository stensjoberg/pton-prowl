import React, { Component } from 'react'
import Radium from 'radium';
import { NavLink } from 'react-router-dom'
import LogoutForm from './LogoutForm'
import { styles } from './styles'
import './css/stylesheet.css'
import './css/normalize.css'
import './css/skeleton.css'

class NavBar extends Component {

  handleLogout = async (event) => {
    localStorage.removeItem('token')
    this.props.history.push('/login')
  }

    render() {
        return (
            <ul className="navbar">
                <li><NavLink to={'/home'} activeClassName="active" key={'home'}>Home</NavLink></li>
                <li style={{float: 'right'}}><button onClick={this.handleLogout}>Logout</button></li>
            </ul>

        )
    }
}

export default Radium(NavBar)
