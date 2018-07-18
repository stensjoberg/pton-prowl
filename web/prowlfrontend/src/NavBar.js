import React, { Component } from 'react'
import Radium from 'radium';
import { NavLink } from 'react-router-dom'
import LogoutForm from './LogoutForm'
import { styles } from './styles'
import './css/stylesheet.css'
import './css/normalize.css'
import './css/skeleton.css'

class NavBar extends Component {

    render() {
        return (
            <div className="navbar">
                <NavLink to={'/'} activeClassName="active" key={'home'}>Home</NavLink>
                <NavLink to={'/'+this.props.user.netid} activeClassName="active" className="profilenav" key={'profile'}>{this.props.user.netid}</NavLink>
                <LogoutForm history={this.props.history}/>
            </div>

        )
    }
}

export default Radium(NavBar) 
