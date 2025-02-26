<template>
    <!-- Dialog-Container mit Transition -->
    <transition name="dialog-fade">
        <div v-show="visible" class="dialog-mask" @click.self="handleClose" role="dialog">
            <div class="dialog-wrapper">
                <div class="dialog-container">
                    <!-- Dialog-Header -->
                    <div class="dialog-header">
                        <slot name="header">
                            <h3>{{ title }}</h3>
                        </slot>
                    </div>

                    <!-- Dialog-Inhalt -->
                    <div class="dialog-body">
                        <slot name="content">{{ content }}</slot>
                    </div>

                    <!-- Dialog-Footer mit Aktionen -->
                    <div class="dialog-footer">
                        <slot name="footer">
                            <button class="dialog-btn cancel" @click="handleCancel">
                                {{ cancelText }}
                            </button>
                            <button class="dialog-btn confirm" @click="handleConfirm">
                                {{ confirmText }}
                            </button>
                        </slot>
                    </div>
                </div>
            </div>
        </div>
    </transition>
</template>

<script>
export default {
    name: 'ConfirmationDialog',
    props: {
        visible: {
            type: Boolean,
            default: false
        },
        title: {
            type: String,
            default: 'Bestätigung erforderlich'
        },
        content: {
            type: String,
            default: 'Möchten Sie diese Aktion wirklich durchführen?'
        },
        cancelText: {
            type: String,
            default: 'Abbrechen'
        },
        confirmText: {
            type: String,
            default: 'Bestätigen'
        },
        closeOnClickModal: {
            type: Boolean,
            default: true
        }
    },
    watch: {
        visible(val) {
            if (val) {
                document.addEventListener('keydown', this.handleKeydown)
            } else {
                document.removeEventListener('keydown', this.handleKeydown)
            }
        },
    },
    methods: {
        handleCancel() {
            console.log("Cancel");
            this.$emit('cancel')
        },
        handleConfirm() {
            console.log("Confirm");
            this.$emit('confirm');
        },
        handleClose() {
            console.log("Close");
            this.$emit('update:visible', false)
            this.$emit('cancel')
        },
        handleKeydown(event) {
            if(event.key === "Escape"){       
                console.log("cancel");
                this.$emit('cancel')
            }
            else if(event.key === "Enter") {
                console.log("enter");
                this.$emit('confirm');
            }
        }
    }
}
</script>

<style scoped>
template {
    display: block;
}

.dialog-mask {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.65);
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: opacity 0.3s ease;
}

.dialog-wrapper {
    max-width: 500px;
    width: 90%;
    margin: 0 auto;
}

.dialog-container {
    background: #fff;
    border-radius: 4px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.dialog-header {
    padding: 20px;
    border-bottom: 1px solid #eee;
}

.dialog-body {
    padding: 20px;
    font-size: 16px;
}

.dialog-footer {
    padding: 20px;
    text-align: right;
    border-top: 1px solid #eee;
}

.dialog-btn {
    padding: 8px 16px;
    margin-left: 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: all 0.3s;
}

.dialog-btn.cancel {
    background: #f5f5f5;
    color: #606266;
}

.dialog-btn.confirm {
    background: #409eff;
    color: white;
}

.dialog-fade-enter-active,
.dialog-fade-leave-active {
    transition: opacity 0.3s;
}

.dialog-fade-enter,
.dialog-fade-leave-to {
    opacity: 0;
}
</style>
