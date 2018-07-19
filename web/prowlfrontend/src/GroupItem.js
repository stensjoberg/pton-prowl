import React, { Component } from 'react'
import Radium from 'radium'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class GroupItem extends Component {

    handleButton = async (event) => {
        event.preventDefault()
        try {
            const res = await fetch('http://0.0.0.0:8000/api/v1/groups/', {
                method: 'POST',
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem('token'),
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    id: this.props.id,
                    change: (this.props.change ? 'enroll' : 'unenroll'),
                })
            })
            if (typeof this.props.onChange === 'function') {
                 this.props.onChange(this.props.id, this.props.change)
            }
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div className="flexcontainer hor coursebox" style={Object.assign({},
                this.props.i % 2 && styles.tigerStripe
            )}>
            <p>
            Group #{this.props.id}
            </p>
            <p>
            Members: {this.props.users.length}
            </p>
            {
                this.props.change
                ? <button onClick={this.handleButton}>+</button>
                : <button onClick={this.handleButton}>-</button>
            }
            </div>
        );
    }
}

export default Radium(GroupItem)
