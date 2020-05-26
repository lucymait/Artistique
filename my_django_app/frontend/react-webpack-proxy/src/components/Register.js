import React from 'react'
// import axios from 'axios'

const Register = () => {
  // const [data, setData] = useState([])

  // handleChange(event) {
  //   const { name, value } = event.target
  //   const data = { ...this.state.data, [name]: value }
  //   this.setState({ data })
  //   console.log(this.state.data)
  // }

  // handleSubmit(event) {
  //   event.preventDefault()
  //   axios.post('/api/register',
  //     this.state.data)
  //     .then(() => this.props.history.push('/login'))
  //     .catch(err => this.setState({ errors: err.response.data.errors }))
  // }

  return <section className="section">
    <div className="container register">
      <h1 className="title register">Register</h1>
      <form
        className="form"
        // onSubmit={(event) => this.handleSubmit(event)}
      >
        <div className="field">
          <div className="control has-icons-left has-icons-right">
            <input
              // onChange={(event) => this.handleChange(event)}
              type="text"
              name="email"
              className="input is-rounded"
              placeholder="Email"
            />
            <span className="icon is-small is-left">
              <i className="fas fa-envelope"></i>
            </span>
            <span className="icon is-small is-right">
              <i className="fas fa-check"></i>
            </span>
          </div>
        </div>
        <div className="field">
          <div className="control has-icons-left has-icons-right">
            <input
              // onChange={(event) => this.handleChange(event)}
              type="text"
              name="username"
              className="input is-rounded"
              placeholder="Username"
            />
            <span className="icon is-small is-left">
              <i className="fas fa-user"></i>
            </span>
            <span className="icon is-small is-right">
              <i className="fas fa-check"></i>
            </span>
          </div>
        </div>
        <div className="field">
          <div className="control has-icons-left has-icons-right">
            <input
              // onChange={(event) => this.handleChange(event)}
              type="password"
              name="password"
              className="input is-rounded"
              placeholder="Password"
            />
            <span className="icon is-small is-left">
              <i className="fas fa-lock"></i>
            </span>
            <span className="icon is-small is-right">
              <i className="fas fa-check"></i>
            </span>
          </div>
        </div>
        <div className="field">
          <div className="control has-icons-left has-icons-right">
            <input
              // onChange={(event) => this.handleChange(event)}
              type="password"
              name="passwordConfirmation"
              className="input is-rounded"
              placeholder="Confirm Password"

            />
            <span className="icon is-small is-left">
              <i className="fas fa-lock"></i>
            </span>
            <span className="icon is-small is-right">
              <i className="fas fa-check"></i>
            </span>
          </div>
        </div>
        <button className="button is-success"
        >Register
        </button>
      </form>
    </div>
  </section>

}

export default Register