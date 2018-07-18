import React, { Component } from 'react'
import Radium from 'radium'
import { getUser } from './helper'
import Availability from './Availability.js'
import NavBar from './NavBar'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class UserDetail extends Component {

    state = {
        user: {}
    };

    async componentDidMount() {
        const netid = this.props.match.params.netid
        const user = await getUser(netid)
        this.setState({
            user
        })
    }

    render() {
        if (this.state.user.availability === undefined) {
            return false
        }
        else {
            return (
                <div>
                <NavBar user={this.state.user} history={this.props.history}/>

                <Availability data={this.state.user.availability}/>
                </div>
            )
        }
    }
}

export default Radium(UserDetail)
