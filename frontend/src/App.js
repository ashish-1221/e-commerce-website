import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
function App() {
  return (
    <>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">Django Market Place</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <a className="nav-link" aria-current="page" href="#">Home</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Categories</a>
              </li>
            </ul>
          
          </div>
        </div>
      </nav>
      <main className='mt-4'>
        <div className="container">
          <div className='row'>
            <div className='col-12 col-md-3 mb-2'>
              <div className="card">
                <img src={logo} class="card-img-top" alt="..."/>
                <div className="card-body">
                  <h5 className="card-title">Product title</h5>
                </div>
              </div>
              <div className='card-footer'></div>
          </div>
        </div>  
      </div>
      </main>
    </>
    );
}

export default App;
