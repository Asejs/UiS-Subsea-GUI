const rovC = {
    props: ['tid', 'teller', 'strom1', 'strom2', 'spenn', 'dybde', 'temp_vann'],
    name: 'rov',
    template: `

    <div class="row">

    <div class="col"><h2>ROV</h2>
        <p class="small">Tid: <span class="badge badge-secondary" id="tid1">{{ tid }}</span></p>
        <p class="small">Teller: <span class="badge badge-secondary" id="tel1">{{ teller }}</span></p>
        <p class="small">Strøm 1: <span  class="badge badge-secondary" id="strom2">{{ strom1 }}</span></p>
        <p class="small">Strøm 2: <span class="badge badge-secondary" id="strom1">{{ strom2 }}</span></p>
        <p class="small">Spenning: <span class="badge badge-secondary" id="spenn1">{{ spenn }}</span></p>
        <p class="small">Orientering: <span class="badge badge-secondary" id="ori"> ------- </span></p>
        <p class="small">Skalering: <span class="badge badge-secondary" id="skall"> ------- </span></p>
    </div>
    
    <div class="col">
        <h3></h3>
            <div class="pb-3">
            <form>
                <div class="custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="rov_btn_1">
                    <label class="custom-control-label" for="rov_btn_1">Manipultor</label>
                </div>
    
            </form>
                <form>
                <div class="custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="rov_btn_2">
                    <label class="custom-control-label" for="rov_btn_2">Lys</label>
                </div>
    
            </form>
                <form>
                <div class="custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="rov_btn_3">
                    <label class="custom-control-label" for="rov_btn_3">Dybde regulator</label>
                </div>
    
            </form>
                <form>
                <div class="custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="rov_btn_4">
                    <label class="custom-control-label" for="rov_btn_4">Vippe regulator</label>
                </div>
    
            </form>
                <form>
                <div class="custom-control custom-switch">
                    <input type="checkbox" class="custom-control-input" id="rov_btn_5">
                    <label class="custom-control-label" for="rov_btn_5">Helnings regulator</label>
                </div>
            </form>
                </div>
    
            <p class="small">Dybde: <span class="badge badge-secondary" id="dybd">{{ dybde }}</span></p>
            <p class="small">Temp vann: <span class="badge badge-secondary" id="vanntemp">{{ temp_vann }}</span></p>
    
        <!--<p>Akselerasjon: <span class="badge badge-secondary" id="aks"> ------- </span></p> -->
    </div>  
    
    </div>
    `,
    data: function() {
        return {
        };
    },
}