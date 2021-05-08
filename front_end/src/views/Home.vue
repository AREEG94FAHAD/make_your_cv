<template>
  <div class="container back">
    <div class="row pt-5">
      <div class="col-3 col-md-4 ">
        <label for="fullname">Full Name <span style="color:red">*</span></label>
      </div>
      <div class="col">
        <div class="form-group">
          <div class="row">
            <div class="col">
              <input
                value=""
                maxlength="25"
                type="text"
                v-model="name"
                class="form-control"
                id="fullname"
                aria-describedby="emailHelp"
                placeholder="Max characters 25"
                required
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-3 col-md-4">
        <label for="exampleFormControlTextarea1"
          >Aboute me <span style="color:red">*</span></label
        >
      </div>
      <div class="col">
        <div class="form-group">
          <div class="row">
            <div class="col">
              <textarea
                value=""
                maxlength="250"
                class="form-control"
                id="exampleFormControlTextarea1"
                rows="3"
                v-model="abouteme"
                placeholder="Max characters 250"
                required
              ></textarea>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-3 col-md-4">
        <label for="ac"
          >Acadmic Background <span style="color:red">*</span></label
        >
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in acadmicBackground"
          :key="index"
        >
          <div class="row">
            <div class="col-8">
              <input
                value=""
                maxlength="50"
                type="text"
                v-model="acadmicBackground[index].unversity"
                class="form-control"
                id="ac"
                aria-describedby="emailHelp"
                placeholder="University (Max 50)"
                required
              />
              <input
                value=""
                maxlength="50"
                type="text"
                v-model="acadmicBackground[index].depart"
                class="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                placeholder="Ex: Msc in Network engineering"
                required
              />
            </div>

            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="add(index)"
                v-show="index == acadmicBackground.length - 1 && index < 2"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="remove(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Experience -->
    <div class="row">
      <div class="col-3 col-md-4">
        <label for="experience"
          >Experience <span style="color:red">*</span></label
        >
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in experience"
          :key="'A' + index"
        >
          <div class="row">
            <div class="col-8">
              <input
                value=""
                maxlength="75"
                type="text"
                v-model="experience[index].experience"
                class="form-control"
                id="experience"
                aria-describedby="emailHelp"
                placeholder="Max 75"
                required
              />
            </div>
            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="addexperience(index)"
                v-show="index == experience.length - 1 && index < 3"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="removeexperience(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- skils -->
    <div class="row">
      <div class="col-3 col-md-4">
        <label for="skill">Skills <span style="color:red">*</span></label>
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in skills"
          :key="'C' + index"
        >
          <div class="row">
            <div class="col-8 ">
              <input
                value=""
                maxlength="35"
                type="text"
                v-model="skills[index].skill"
                class="form-control"
                id="skill"
                aria-describedby="emailHelp"
                placeholder="Max characters 35"
              />
            </div>
            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="addskill(index)"
                v-show="index == skills.length - 1 && index < 9"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="removeskill(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Certifcates -->

    <div class="row">
      <div class="col-3 col-md-4">
        <label for="certifcate"
          >Certifcates<span style="color:red">*</span></label
        >
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in certifcates"
          :key="'D' + index"
        >
          <div class="row">
            <div class="col-8">
              <input
                value=""
                maxlength="40"
                type="text"
                v-model="certifcates[index].certifcate"
                class="form-control"
                id="certifcate"
                aria-describedby="emailHelp"
                placeholder="Max (40)"
              />
            </div>
            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="addcertifcate(index)"
                v-show="index == certifcates.length - 1 && index < 4"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="removecertifcate(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Accomplishments -->
    <div class="row">
      <div class="col-3 col-md-4">
        <label for="accomplishment">Accomplishments</label>
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in accomplishments"
          :key="'E' + index"
        >
          <div class="row">
            <div class="col-8">
              <input
                value=""
                maxlength="100"
                type="text"
                v-model="accomplishments[index].accomplishment"
                class="form-control"
                id="accomplishment"
                aria-describedby="emailHelp"
                placeholder="Max (100)"
              />
            </div>
            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="addaccomplishment(index)"
                v-show="index == accomplishments.length - 1 && index < 2"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="removecaccomplishment(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Contact Info -->
    <div class="row">
      <div class="col-3 col-md-4">
        <label for="accomplishment"
          >Contact Info<span style="color:red">*</span></label
        >
      </div>
      <div class="col">
        <div
          class="form-group"
          v-for="(input, index) in contactinfo"
          :key="'f' + index"
        >
          <div class="row">
            <div class="col-3 px- pt-2">
              <select
                v-model="contactinfo[index].type"
                style="color:gray"
                required
              >
                <option disabled value="">Account</option>
                <option v-for="item in account" :value="item" :key="item">
                  {{ item }}
                </option>
              </select>
            </div>
            <div class="col-5">
              <input
                value=""
                maxlength="100"
                type="text"
                v-model="contactinfo[index].acount"
                class="form-control"
                id="accomplishment"
                aria-describedby="emailHelp"
                placeholder=""
              />
            </div>
            <div class="col-4 item" id="centerButton">
              <button
                class="btn btn btn-info"
                @click="addaccount(index)"
                v-show="index == contactinfo.length - 1 && index < 4"
              >
                <span class="fas fa-plus-circle"></span>
              </button>
              <button
                class="btn btn-danger"
                @click="removeaccount(index)"
                v-show="index != 0"
              >
                <span class="fas fa-trash"></span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-4">
        <label for="image">Choose Iamge</label>
      </div>
      <div class="col">
        <div class="form-group">
          <input
            id="image"
            type="file"
            ref="fileupload"
            name="file"
            @change="onFileSelected"
          />
        </div>
      </div>
    </div>

    <button class="btn btn-info" @click="submitForm()">Create CV</button
    >{{ "   " }}
    <button class="btn btn-danger" @click="eraser()">ضد القشرة Clear</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",

  components: {},
  data() {
    return {
      name: "",
      checkImage: false,
      ll: "",
      selectedFile: null,
      abouteme: "",
      acadmicBackground: [
        {
          unversity: "",
          depart: "",
        },
      ],
      experience: [
        {
          experience: "",
        },
      ],
      skills: [
        {
          skill: "",
        },
      ],
      certifcates: [
        {
          certifcate: "",
        },
      ],
      contactinfo: [
        {
          type: "",
          acount: "",
        },
      ],
      account: ["Email", "Linked in", "Github", "Facebook", "website"],
      accomplishments: [
        {
          accomplishment: "",
        },
      ],
    };
  },
  methods: {
    eraser() {
      this.name = "";
      this.abouteme = "";
      this.acadmicBackground = [{}];
      this.experience = [{}];
      this.skills = [{}];
      this.certifcates = [{}];
      this.$refs.fileupload.value = null;

      this.accomplishments = [{}];
    },
    onFileSelected(event) {
      if (event.target.files[0].size > 600000) {
        alert("Image Size more 500KB");
        this.$refs.fileupload.value = null;
        this.selectedFile = "";
      }

      this.selectedFile = event.target.files[0];
      this.checkImage = true;

      console.log(event);
    },
    add() {
      this.acadmicBackground.push({
        unversity: "",
        depart: "",
      });
      console.log(this.acadmicBackground);
    },
    remove(index) {
      this.acadmicBackground.splice(index, 1);
    },

    addexperience() {
      this.experience.push({
        experience: "",
      });
      console.log(this.experience);
    },
    removeexperience(inde) {
      this.experience.splice(inde, 1);
    },
    addskill() {
      this.skills.push({
        skill: "",
      });
      console.log(this.skils);
    },
    removeskill(inde) {
      this.skills.splice(inde, 1);
    },
    addcertifcate() {
      this.certifcates.push({
        certifcate: "",
      });
      console.log(this.certifcates);
    },
    removecertifcate(inde) {
      this.certifcates.splice(inde, 1);
    },
    addaccomplishment() {
      this.accomplishments.push({
        accomplishment: "",
      });
      console.log(this.accomplishment);
    },
    removecaccomplishment(index) {
      this.accomplishments.splice(index, 1);
    },
    addaccount() {
      this.contactinfo.push({
        type: "",
        acount: "",
      });
      console.log(this.contactinfo);
    },
    removeaccount(inde) {
      this.contactinfo.splice(inde, 1);
    },

    submitForm() {
      console.log(this.acadmicBackground.length);
      if (
        this.name == "" ||
        this.abouteme == "" ||
        this.acadmicBackground.length < 1 ||
        this.experience.length < 1 ||
        this.skills.length < 1 ||
        this.certifcates.length < 1 ||
        this.contactinfo.length < 1
      ) {
        alert("Please fill in all required items");
        return 0;
      }
      const fd = new FormData();
      if (this.selectedFile != null) {
        fd.append("image", this.selectedFile);
      }
      fd.append("checkImage", JSON.stringify(this.checkImage));
      fd.append("name", JSON.stringify(this.name));
      fd.append("abouteme", JSON.stringify(this.abouteme));
      fd.append("acadmicBackground", JSON.stringify(this.acadmicBackground));
      fd.append("experience", JSON.stringify(this.experience));
      fd.append("skills", JSON.stringify(this.skills));
      fd.append("certifcates", JSON.stringify(this.certifcates));
      fd.append("contactinfo", JSON.stringify(this.contactinfo));
      fd.append("accomplishments", JSON.stringify(this.accomplishments));
      // this.name="";
      // this.abouteme="";
      // this.acadmicBackground=[{}];
      // this.experience=[{}];
      // this.skills=[{}];
      // this.certifcates=[{}];
      // // this.contactinfo=[{}];
      // this.accomplishments=[{}];

      // axios.post("http://127.0.0.1:5000/", fd, {}).then((response) => {
      axios
        .post("http://127.0.0.1:5000/", fd, {
          responseType: 'blob'
        })
          .then(response => response.data)
    .then(blob => {
      const data = URL.createObjectURL(blob)
      var link = document.createElement('a')
      link.href = data
      link.target = '_blank'
      link.click()
      window.URL.revokeObjectURL(blob)
    })
    .catch((error) => {
      console.log(error)
    })
        // .then((response) => {
        //   console.log(response);
        //   var fileURL = URL.createObjectURL(new Blob([response.data]));
        //   var fileLink = document.createElement("a");

        //   fileLink.href = fileURL;
        //   fileLink.target='_blank'
        //   fileLink.click();
        //   // fileLink.setAttribute(
        //   //   "download",
        //   //   this.name + new Date().toISOString().slice(0, 10) + ".pdf"
        //   // );
        //   // document.body.appendChild(fileLink);
          
        //   window.URL.revokeObjectURL(response);
        // });
    },
  },
};
</script>

<style scoped>
.col-2,
.col-8,
.col,
.col-3,
.col-4,
div.col-4 {
  padding: 2;
  text-align: left;
}
#centerButton {
  text-align: center;
}
.item {
  order: 2; /* default is 0 */
  padding: 0px;
  text-align: center;
  margin-top: 2px;
}
button {
  font-size: revert;
}

.back {
  background: rgba(247, 248, 247, 0.9); /* Green background with 30% opacity */
  margin-top: 20px;
  padding: 16px;
  /* height: 10% !; */
}
</style>
